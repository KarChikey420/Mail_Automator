import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API")
if not api_key:
    raise ValueError("❌ GOOGLE_API not found in .env file")

genai.configure(api_key=api_key)

try:
    # Use a free model like gemini-2.0-flash or gemini-2.5-flash-lite
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    response = model.generate_content("Hello! Just testing if the API key works. Reply with 'Success'.")
    print("✔ API Key is valid!")
    print("Response:", response.text)

except Exception as e:
    print("❌ API Key is invalid or request failed.")
    print("Error:", e)
