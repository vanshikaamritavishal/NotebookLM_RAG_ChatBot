# NotebookLM RAG Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot inspired by Google NotebookLM.

Users can upload PDF or TXT documents and ask natural language questions about the uploaded content. The chatbot retrieves relevant chunks from the document using vector similarity search and generates grounded responses using an LLM.

---

# Features

- Upload PDF or TXT documents
- Automatic text chunking
- Embedding generation using Sentence Transformers
- Vector similarity search using FAISS
- Context-aware question answering
- FastAPI backend
- Simple and clean frontend
- Grounded responses from uploaded documents only

---

# Tech Stack

## Backend
- Python
- FastAPI
- FAISS
- Sentence Transformers
- Groq API

## Frontend
- HTML
- CSS
- JavaScript

---

# RAG Pipeline

The project implements a complete RAG pipeline:

```text
Document Upload
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Storage
      ↓
Similarity Retrieval
      ↓
LLM Response Generation

```

## Chunking Strategy

The uploaded document is split into overlapping chunks for better retrieval quality.

- Chunk Size: 1000 characters
- Overlap: 200 characters

This improves contextual continuity and retrieval accuracy.

---

# Project Structure

```text
NotebookLM-RAG/
│
├── backend/
│   ├── __pycache__/
│   ├── .env
│   ├── main.py
│   ├── rag.py
│   ├── requirements.txt
│   └── utils.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── uploads/
├── venv/
└── .gitignore
```

# Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## 2. Navigate Into Project

```bash
cd NotebookLM-RAG
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the `backend` folder:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from:

https://console.groq.com

---

# Running the Backend

Navigate into backend folder:

```bash
cd backend
```

Run:

```bash
python main.py
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Open:

```text
frontend/index.html
```

in your browser.

---

# API Endpoints

## Upload Document

```http
POST /upload
```

Uploads a PDF or TXT file.

---

## Ask Question

```http
POST /ask
```

Request body:

```json
{
  "question": "What is this document about?"
}
```

---

# Example Use Cases

- Resume Q&A
- FAQ Assistant
- Research Paper Assistant
- Notes Assistant
- Documentation Chatbot

---

# Deployment

## Backend

Deployed using Render.

## Frontend

Deployed using Vercel.

---

# Limitations

- Single document support
- No chat history
- Basic retrieval strategy
- No authentication

---

# Future Improvements

- Multi-document support
- Streaming responses
- Better chunking strategies
- Hybrid search
- Conversation memory
- Authentication system

---

# Author

Vanshika Amrita Vishal
