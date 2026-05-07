from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypdf import PdfReader

from rag import chunk_text, store_chunks, retrieve
from utils import ask_llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/upload")

async def upload_file(file: UploadFile = File(...)):

    text = ""

    if file.filename.endswith(".pdf"):

        reader = PdfReader(file.file)

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    elif file.filename.endswith(".txt"):

        contents = await file.read()

        text = contents.decode("utf-8")

    else:
        return {"error": "Only PDF and TXT supported"}

    chunks = chunk_text(text)

    store_chunks(chunks)

    return {
        "message": "Document uploaded successfully",
        "chunks": len(chunks)
    }

@app.post("/ask")

def ask(q: Question):

    context = retrieve(q.question)

    answer = ask_llm(q.question, context)

    return {
        "answer": answer
    }

@app.get("/")

def home():
    return {"message": "NotebookLM RAG API Running"}


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)