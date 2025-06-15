import streamlit as st
import openai
import chromadb
from chromadb.config import Settings
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# ChromaDB laden
client = chromadb.Client(Settings(persist_directory="db"))
collection = client.get_collection("docs")

def retrieve(query):
    # Suche nach den relevantesten Chunks (Embedding-Vergleich)
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return [doc for doc in results['documents'][0]]

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Nutze diese Information:\n{context}\n\nFrage: {query}\nAntwort:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("RAG-Chatbot mit ChromaDB")
user_input = st.text_input("Stelle deine Frage:")

if user_input:
    context = retrieve(user_input)
    answer = generate_answer(user_input, context)
    st.write("**Antwort:**", answer)
