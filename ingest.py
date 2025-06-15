import chromadb
from chromadb.config import Settings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Dokument einlesen (z. B. aus data/example.txt)
with open("data/example.txt", "r", encoding="utf-8") as f:
    text = f.read()

# In kleine Chunks teilen
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(text)

# ChromaDB initialisieren
client = chromadb.Client(Settings(
    persist_directory="db"  # für persistente Speicherung
))
collection = client.get_or_create_collection("docs")

# Dokumente als Embeddings speichern (hier: einfache IDs)
for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        ids=[f"doc_{i}"]
    )
print("Dokumente gespeichert!")
