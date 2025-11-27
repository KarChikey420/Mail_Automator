import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, body):
    try:
        gmail_user = os.getenv("GMAIL_NAME")
        gmail_password = os.getenv("GMAIL_PASSWORD")

        if not gmail_user or not gmail_password:
            print("Missing GMAIL_USER or GMAIL_PASSWORD in .env")
            return False

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, "plain"))

        print("Connecting to smtp.gmail.com...")
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()  
            server.starttls() 
            server.login(gmail_user, gmail_password)
            server.send_message(msg)

        print("Email sent successfully via SMTP!")
        return True

    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
