# 🧠 RAG-Based Chatbot with Flask & Groq

This project is a **Retrieval-Augmented Generation (RAG)** chatbot built using:

- 🧩 Flask for the web and API interface  
- 🧠 LangChain for chaining LLMs with context  
- 🔍 FAISS for vector similarity search  
- 🏎️ Groq's LLaMA3-8b-8192 as the language model  
- 📚 HuggingFace's all-MiniLM-L6-v2 for embeddings  

It supports both a web interface and a JSON API to answer questions using content from a local text file.

---
## 📁 Project Structure

project/
├── app.py # Flask web and API server
├── docs/
│ └── drivepk.txt # Document used for retrieval
├── src/
│ └── chatbot.py # RAG chain builder logic
├── templates/
│ └── index.html # Web UI template
├── tests/
│ └── test_chatbot.py # Pytest test cases
├── .env # Environment variables
└── README.md # This file


---

## 🚀 Features

- ✅ Retrieval-Augmented Generation (RAG)
- 🧠 LLM via Groq (LLaMA3-8b-8192)
- 📚 Custom document embedding with HuggingFace
- ⚡ Fast vector search using FAISS
- 🖥️ HTML-based web interface
- 📡 JSON API endpoint for integration with tools like Postman

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your Groq API key:
```

### 4. Configure Environment Variables
```bash
Create a .env file in the root directory and add your Groq API key
GROQ_API_KEY=your_groq_api_key_here
```
5. Add Source 
```bash
Make sure you have a file at docs/drivepk.txt. This document will be used for generating context.
▶️ Running the App
Start the Flask server:

bash
python app.py
Web UI: http://localhost:5000

API Endpoint: http://localhost:5000/api/ask
```