from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from vectorstore import retrieve_chunks

load_dotenv()

def get_answer(question):
    docs = retrieve_chunks(question)

    if not docs:
        return "The answer is not available on the provided website."

    context = "\n\n".join(docs)

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. "
                "Answer the user's question using ONLY the provided context. "
                "If the answer is not explicitly present, respond exactly with: "
                "'The answer is not available on the provided website.'"
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{question}"
        }
    ]

    response = llm.invoke(messages)
    return response.content.strip()


def summarize_website(text):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = (
        "Provide a concise 3–4 sentence summary of the following website content. "
        "Do not add any information that is not present in the content.\n\n"
        f"{text[:4000]}"
    )

    response = llm.invoke(prompt)
    return response.content.strip()
