import streamlit as st

from crawler import crawl_web
from chunker import chunk_text
from vectorstore import store_chunks
from rag import get_answer, summarize_website

st.set_page_config(page_title="Website-Based Chatbot")

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "history" not in st.session_state:
    st.session_state.history = []

if "summary" not in st.session_state:
    st.session_state.summary = None

st.title("Website-Based Chatbot")

url = st.text_input("Enter Website URL")

if st.button("Index Website"):
    try:
        title, text = crawl_web(url)

        chunks = chunk_text(
            text,
            metadata={"source": url, "title": title}
        )
        store_chunks(chunks)

        summary = summarize_website(text)

        st.session_state.indexed = True
        st.session_state.summary = summary
        st.session_state.history = []

        st.success("Website indexed successfully")

    except Exception as e:
        st.error(str(e))

st.divider()

if st.session_state.summary:
    st.subheader("Website Summary")
    st.write(st.session_state.summary)

st.divider()

for role, message in st.session_state.history:
    with st.chat_message(role):
        st.write(message)

if st.session_state.indexed:
    user_input = st.chat_input("Ask something about the website")

    if user_input:
        st.session_state.history.append(("user", user_input))

        with st.chat_message("assistant"):
            answer = get_answer(user_input)
            st.write(answer)

        st.session_state.history.append(("assistant", answer))
