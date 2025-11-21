import imaplib
import email
import os
from dotenv import load_dotenv

load_dotenv()

def unread_email_fetcher():
    try:
        mail=imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(os.getenv("GOOGLE_USERNAME"),os.getenv("GOOGLE_PASSWORD"))
        mail.select("inbox")
        
        print("Fetching Unread Emails...")
        _, search_data=mail.search(None,'(UNSEEN)')
        email_list=[]
        
        for num in search_data[0].split():
            _, data=mail.fetch(num,'(RFC822)')
            raw_email=data[0][1]
            msg=email.message_from_bytes(raw_email)
            email_list.append(msg)
            
            sender=email.utils.parseaddr(msg.get("From"))[1]
            subject=msg.get("Subject")
            
            body=""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type()=="text/plain":
                        body=part.get_payload(decode=True).decode()
                        break
            else:
                body=msg.get_payload(decode=True).decode()
            email_list.append({
                "Sender": sender,
                "Subject":subject,
                "Body":body
            })
            mail.store(num,'+FLAGES','\\Seen')
            
        print(f"Total Unread Emails:{len(email_list)}")
        return email_list
    except Exception as e:
        print("Error:",str(e))
        return []
    
