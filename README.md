# Multi-Modal Chatbot
This project demonstrate how to build a chatbot capable of processing and describing images.

This could be considered as a successor to my other project [llm-chatbot](https://github.com/kayaozan/llm-chatbot) which you might want to check out.

## Dependencies
The script is written in Python. The required software and libraries are as following:
- [Ollama](https://ollama.com/): Lets the user to run LLMs. It is installed locally and the LLM used in this project is downloaded.
- [LLaVA](https://ollama.com/library/llava): A multimodal model that combines a vision encoder and Vicuna for general-purpose visual and language understanding.
- [Ollama Python Library](https://github.com/ollama/ollama-python): Provides the integration of Python with Ollama.
- [Streamlit](https://streamlit.io/): The library to build the chatbot app.

## Breakdown
- The user is asked to provide a prompt.
- If desired, an image is selected locally with the `file_uploader` module of streamlit.
- The prompt and the image are sent to the model as a package.
- All messaging history is saved and shown in real time.

## Final Look
Here is how the page looks once the script is run by streamlit in a web browser.

User can upload an image as seen on the right side. The chat stream is demonstrated on the other side.

![Screenshot 2025-02-10 201333](https://github.com/user-attachments/assets/abd83b08-c9eb-4de2-bad5-1d14496342c2)
