import streamlit as st
from dotenv import load_dotenv
import torch
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import  HuggingFaceBgeEmbeddings
from InstructorEmbedding import INSTRUCTOR
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=512,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm =llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="MyDocGPT - Chat with your PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Initialize flag to 0
    flag = 0

    st.header("MyDocGPT :books:", divider='rainbow')

    with st.sidebar:
        st.subheader("Upload Files :file_folder:")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if len(pdf_docs)!=0:
            # Update flag to 1 when files are uploaded
            flag = 1
        if len(pdf_docs)>5:
            flag = 2
        
        if st.button("Process"):
            if flag == 1:
                with st.spinner("Processing"):
                    # get pdf text
                    raw_text = get_pdf_text(pdf_docs)
                    # get the text chunks
                    text_chunks = get_text_chunks(raw_text)

                    # create vector store
                    vectorstore = get_vectorstore(text_chunks)

                    # create conversation chain
                    st.session_state.conversation = get_conversation_chain(
                        vectorstore)
                    st.success("File Processed:white_check_mark:")
            if flag == 2:
                st.warning("File Upload limit exceeded:heavy_exclamation_mark:")
                st.warning("You can only upload upto 5 files.")
           
            if flag ==0:
                st.warning("No files uploaded:heavy_exclamation_mark:")

    user_question = st.chat_input("Ex: What is the document about?")
    if user_question:
        if flag == 0:
            st.warning("Please upload a file before asking questions:heavy_exclamation_mark:")
        else:
            handle_userinput(user_question)




if __name__ == '__main__':
    main()

#streamlit run app.py
