import google.generativeai as genai
import os
from dotenv import load_dotenv
from chroma_db import store_emails_in_vector_db
from spam_or_not import spam_or_not

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API'))

# def generte_response(email_data):

#     if spam_or_not(email_data["Body"]):
#         print(f"Email from {email_data['Sender']} classified as Spam. No response generated.")
#         return None, "spam"
    
#     tone_instruction = "Use a professional and polite tone."

#     query = (
#         f"{tone_instruction}\n"
#         f"Generate a concise and professional reply.\n"
#         f"Do not mention AI.\n"
#         f"Email From: {email_data['Sender']}\n"
#         f"Email Subject: {email_data['Subject']}\n"
#         f"Body:\n{email_data['Body']}\n"
#     )

#     model = genai.GenerativeModel("gemini-1.5-flash")

#     result = model.generate_content(query)
#     context = result.text if result else "No relevant past email context."

#     final_prompt = f"""
#         You are an email assistant.

#         ### Context:
#         {context}

#         ### Current Email Details:
#         {query}

#         Now write the final email reply in proper professional format.
#         Ensure:
#         - Tone is polite and professional
#         - Reply is concise
#         - Do NOT mention that you are an AI
#         - Add a polite closing line
#         """

#     response = model.generate_content(final_prompt)
#     return response.text.strip(), "not_spam"
def generte_response(email_data):
    tone_instruction = "Use a professional and polite tone."

    query = (
        f"{tone_instruction}\n"
        f"Generate a concise reply.\n"
        f"Email From: {email_data['Sender']}\n"
        f"Email Subject: {email_data['Subject']}\n"
        f"Body:\n{email_data['Body']}\n"
    )

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)

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
