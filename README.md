# PDF_Chatbot
Chat with your own data
The PDF_Chatbot App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a Open-source large language model from Huggingface hub to generate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

# How it works
1) The application follows these steps to provide responses to your questions:
2) PDF Loading: The app reads multiple PDF documents and extracts their text content.
3) Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.
4) Language Model: The application utilizes a open-source language model (BAAI/bge-small-en-v1.5) to generate vector representations (embeddings) of the text chunks.
5) Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.
6) Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

# Installation
To install the App, please follow these steps:

Clone the repository to your local machine.
Install the required dependencies by running the following command:

pip install -r requirements.txt

Obtain an API key from HUGGINGFACE_HUB and add it to the .env file in the project directory.

HUGGINGFACEHUB_API_TOKEN = "YOUR SECRET KEY"

# Usage
To use the MultiPDF Chat App, follow these steps:
Ensure that you have installed the required dependencies and added the Huggingface API key to the .env file.
Run the main.py file using the Streamlit CLI. Execute the following command:

streamlit run app.py

The application will launch in your default web browser, displaying the user interface.
Load multiple PDF documents into the app by following the provided instructions.
Ask questions in natural language about the loaded PDFs using the chat interface.

# License
PDF_Chatbot App is licensed under MIT License
