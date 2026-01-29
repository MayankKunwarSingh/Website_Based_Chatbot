def chunk_text(text, chunk_size=500, overlap=100, metadata=None):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append({"text": chunk, "metadata": metadata})
        start += chunk_size - overlap

    return chunks
