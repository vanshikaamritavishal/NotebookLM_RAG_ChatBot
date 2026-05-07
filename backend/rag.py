import faiss
import numpy as np
from utils import get_embeddings

documents = []

index = faiss.IndexFlatL2(384)

def chunk_text(text, chunk_size=1000, overlap=200):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def store_chunks(chunks):

    global documents

    documents = chunks

    embeddings = get_embeddings(chunks)

    embeddings = np.array(embeddings).astype("float32")

    index.reset()

    index.add(embeddings)

def retrieve(query, k=5):

    query_embedding = np.array(
        [get_embeddings([query])[0]]
    ).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return "\n".join(results)