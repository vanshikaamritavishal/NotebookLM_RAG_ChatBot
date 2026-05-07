import os
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

embedding_model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_embedding(text):
    return embedding_model.encode(text).tolist()

def get_embeddings(texts):
    return embedding_model.encode(texts).tolist()

def ask_llm(question, context):

    prompt = f"""
You are a document question-answering assistant.

Answer ONLY using the provided context.

Formatting rules:
- Use bullet points when listing more than 1 items
- Keep answers clean and readable
- If multiple items exist, show all of them
- Do not hallucinate information

If the answer contains multiple items, list ALL of them clearly.

If the answer is not found in the context, say:
"I could not find that information in the document."

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