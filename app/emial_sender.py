import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email,subject,body):
    try:
        msg=MIMEMultipart()
        msg['From']=os.getenv("GOOGLE_USERNAME")
        msg['TO']=to_email
        msg['suject']=subject
        
        with smtplib.SMTP('smtp.gmail.com',587) as server:
            server.login(os.getenv("GOOGLE_USERNAME"),os.getenv("GOOGLE_PASSWORD"))
            server.send_message(msg)
        
        print("Email sent successfully!")
        return True
    except Exception as e:
        print("Error:",str(e))
        return False
    