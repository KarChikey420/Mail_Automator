import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API'))

def spam_or_not(email_text):
    model = genai.GenerativeModel('gemini-flash')
    