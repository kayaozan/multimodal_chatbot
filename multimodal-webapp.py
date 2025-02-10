import streamlit as st

from ollama import chat
import logging

logging.basicConfig(level=logging.INFO)

# Initialize chat history in session state.
if 'messages' not in st.session_state:
    st.session_state.messages = []

def generate_response(model,
                      messages):
    """Stream chat response."""
    try:
        response = ''
        response_placeholder = st.empty()
        # Append the response to the output
        for r in chat(model, messages, stream=True):
            response += r['message']['content']
            response_placeholder.write(response)
        # Log the response
        logging.info(f'Model: {model}, Messages: {prompt}, Response: {response}')
        return response

    except Exception as e:
        logging.error(f'Error during streaming: {str(e)}')
        raise e

st.title('MultiModal LLM Analyzer')
logging.info('App started')

# Define the model.
model = 'llava'

# # Ask for user to upload an image if desired.
with st.sidebar:
    file = st.file_uploader('Add an image',
                            type=['png','jpg'],
                            accept_multiple_files=False)
    if file:
        st.image(file)

# Ask for user input.
prompt = st.chat_input('Add your prompt here.')
if prompt:
    # Append the message of user to the messages.
    # If provided, image will be saved as raw bytes, which the model can handle.
    st.session_state.messages.append({'role': 'user',
                                    'content': prompt,
                                    'images': None if file is None else [file.getvalue()]})
    logging.info(f'User input: {prompt}')

    # Display all messages written so far.
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
            if message['images']:
                st.image(message['images'][0])

    # Generate a new response if the last message is from the user.
    if st.session_state.messages[-1]['role'] != 'assistant':
        with st.chat_message('assistant'):
            logging.info('Generating response')
            with st.spinner('Writing...'):
                try:
                    # Send the messages and get a response.
                    response_message = generate_response(model,
                                                        st.session_state.messages)
                    # Append the response to messages.
                    st.session_state.messages.append({'role': 'assistant',
                                                    'content': response_message,
                                                    'images': None})
                    logging.info(f'Response: {response_message}')

                except Exception as e:
                    st.error('An error occurred while generating the response.')
                    logging.error(f'Error: {str(e)}')