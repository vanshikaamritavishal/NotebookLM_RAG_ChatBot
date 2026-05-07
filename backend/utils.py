import os
from groq import Groq
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

vectorizer = TfidfVectorizer()

stored_chunks = []
stored_vectors = None


def build_vectors(chunks):
    global stored_chunks, stored_vectors

    stored_chunks = chunks
    stored_vectors = vectorizer.fit_transform(chunks)


def retrieve_chunks(question, top_k=3):
    question_vector = vectorizer.transform([question])

    similarities = np.dot(
        stored_vectors,
        question_vector.T
    ).toarray()

    top_indices = similarities.flatten().argsort()[-top_k:][::-1]

    return [stored_chunks[i] for i in top_indices]


def ask_llm(question, context):
    prompt = f"""
You are a helpful document assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content