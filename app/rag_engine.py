import google.generativeai as genai
import os
from dotenv import load_dotenv
from chroma_db import store_emails_in_vector_db
from spam_or_not import spam_or_not

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API'))

def generte_response(email_data):
    tone_instruction = "Use a professional and polite tone."

    query = (
        f"{tone_instruction}\n"
        f"Generate a concise reply.\n"
        f"Email From: {email_data['Sender']}\n"
        f"Email Subject: {email_data['Subject']}\n"
        f"Body:\n{email_data['Body']}\n"
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    final_prompt = f"""
    You are an email assistant.
    Use any relevant past email from the database to respond professionally.

    ### Current Email:
    {query}

    Write final reply:
    - Polite & professional
    - Do NOT mention AI
    - Keep it concise
    - Add polite closing
    """

    result = model.generate_content(final_prompt)
    return result.text.strip(), "not_spam"
