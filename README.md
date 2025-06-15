# RAG-Chatbot mit ChromaDB

Ein Chatbot, der eigene Dokumente durchsucht und Antworten mithilfe von KI generiert.  
Nutzt ChromaDB als Vektor-Datenbank und OpenAI GPT für die Antwortgenerierung.

## Quickstart
1. `pip install -r requirements.txt`
2. Beispiel-Dokument in den `data/` Ordner legen und mit `python ingest.py` indizieren.
3. OpenAI-API-Key in `app.py` eintragen.
4. `streamlit run app.py` starten.

---
