import chromadb
from email_reader import unread_email_fetcher
import google.generativeai as genai
from chromadb.config import Settings
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API'))
chroma_client=chromadb.Client(Settings(persitst_db="email_rag_db"))
collection=chroma_client.get_or_create_collection("emails")

def store_emails_in_vector_db(emails):
    for i,mail in enumerate(emails):
        collection.add(
            documents=[f"Subject: {mail['subject']}\nBody: {mail['body']}\nBody: {mail['body']}"],
            metadatas=[{"sender":mail["Sender"],"subject":mail["Subject"]}],
            ids=[f"email_{i}"]
        )

def generate_response(query):
    
    