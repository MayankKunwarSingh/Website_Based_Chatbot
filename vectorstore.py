from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

client = Client(Settings(persist_directory="chroma_db"))
collection = client.get_or_create_collection(name="website_content")

model = SentenceTransformer("all-MiniLM-L6-v2")

def store_chunks(chunks):
    documents = [c["text"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]
    embeddings = model.encode(documents).tolist()
    ids = [str(abs(hash(doc))) for doc in documents]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

def retrieve_chunks(query, k=4):
    embedding = model.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[embedding], n_results=k)
    return results["documents"][0] if results["documents"] else []
