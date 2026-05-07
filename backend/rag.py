from utils import build_vectors, retrieve_chunks


def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def process_document(text):
    chunks = chunk_text(text)
    build_vectors(chunks)


def get_context(question):
    chunks = retrieve_chunks(question)
    return "\n".join(chunks)