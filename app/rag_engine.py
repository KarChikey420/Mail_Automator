import chromadb
from email_reader import unread_email_fetcher
from chromadb.config import Settings
import os

chroma_client=chromadb.Client(Settings(persitst_db="email_rag_db"))
collection=chroma_client.get_or_create_collection("emails")

def store_emails_in_vector_db(emails):
    for i,mail in enumerate(emails):
        collection.add(
            documents=[f"Subject: {mail['subject']}\nBody: {mail['body']}\nBody: {mail['body']}"],
            metadatas=[{"sender":mail["Sender"],"subject":mail["Subject"]}],
            ids=[f"email_{i}"]
        )
    print(f"Stored {len(emails)} emails in vector database")
    
    