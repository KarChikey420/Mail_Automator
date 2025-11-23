import chromadb
from chromadb.config import Settings

chroma_client=chromadb.Client(Settings(persist_directory="email_rag_db"))
collection=chroma_client.get_or_create_collection("emails")

def store_emails_in_vector_db(emails):
    for i,mail in enumerate(emails):
        collection.add(
            documents=[f"Subject: {mail['Subject']}\nFrom: {mail['Sender']}\nBody: {mail['Body']}"],
            metadatas=[{"sender":mail["Sender"],"subject":mail["Subject"]}],
            ids=[f"email_{i}"]
        )
    print(f"Stored {len(emails)} emails in vector database")
    
    