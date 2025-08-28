import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


def load_env():
    load_dotenv()
    return os.getenv("GROQ_API_KEY")


def load_llm(api_key: str):
    return ChatGroq(model="Llama3-8b-8192", groq_api_key=api_key)


def build_prompt():
    return ChatPromptTemplate.from_template("""
    Answer the question based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    </context>
    Question: {input}
    """)


def create_vectorstore(filepath=None):
    if filepath is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        filepath = os.path.join(current_dir, "../docs", "drivepk.txt")
    loader = TextLoader(filepath, encoding='utf-8')
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(texts, embeddings)
    
    return vectorstore.as_retriever()


def build_rag_chain():
    groq_api_key = load_env()
    llm = load_llm(groq_api_key)
    prompt = build_prompt()
    retriever = create_vectorstore()
    
    qa_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, qa_chain)
    
    return rag_chain


if __name__ == "__main__":
    # Create RAG chain
    rag = build_rag_chain()
