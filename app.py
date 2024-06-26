from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS  # Facebook AI similarity search
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

def main():
    hf_token = "Hugging Face API"
    
    st.set_page_config(page_title="RAG Pipeline")
    st.header("RAG-Powered Chatbot for PDF Question Answering")

    pdf = st.file_uploader("Upload your pdf", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create embedding
        embeddings = HuggingFaceEmbeddings()

        knowledge_base = FAISS.from_texts(chunks, embeddings)

        user_question = st.text_input("Ask Question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            llm = HuggingFaceHub(
                repo_id="google/flan-t5-large",
                huggingfacehub_api_token=hf_token,  
                model_kwargs={"temperature": 5, "max_length": 64}
            )
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_question)

            st.write(response)

if __name__ == '__main__':
    main()
