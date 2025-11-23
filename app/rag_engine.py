import google.generativeai as genai
import os
from dotenv import load_dotenv
from chroma_db import store_emails_in_vector_db
from spam_or_not import spam_or_not

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API'))

def generte_response(email_data):
    
    if spam_or_not(email_data['Body']):
        print(f"Email from {email_data['Sender']} classified as Spam. No response generated.")
        return None,"spam"
    
    tone_instruction="Use a professional and polite tone."
    query=(
        f"{tone_instruction}\n"
        f"generate a consise and professional reply.\n"
        f"Don't metion AI.\n"
        f"Email Subject:{email_data['Sender']}\n"
        f"Subject:{email_data['Subject']}\n"
        f"Body:\n{email_data['Body']}\n"
    )
    result=genai.GenerativeModel("gemini-1.5-flash").generate_content(query)
    context = result.text if result else "No related past emails."
    
    model=genai.GenerativeModel("gemini-1.5-flash")
    final_prompt=""""
        You are an email assistant.
        ### Past Email Context:
        {context}
        
        ### Past Details:
        {query}
      
        Write the reply in proper email format.
        Ensure the tone is polite, concise, and professional.
        Do NOT mention that you are an AI.
        """
    
    response=model.generate_content(final_prompt)
    return response.text.strip(),"not_spam"