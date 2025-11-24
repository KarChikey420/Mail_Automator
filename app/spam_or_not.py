import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API'))

def spam_or_not(email_text):
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""
        Classify the following email content as 'Spam' or 'not Spam'.
        Email Content:"{email_text}"
        Only reply with 'Spam' or 'not Spam'.  
    """
    
    response = model.generate_content(prompt)  
    classification = response.text.strip()
    return classification == 'Spam'
