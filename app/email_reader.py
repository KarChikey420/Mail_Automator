import imaplib
import email
import os
from dotenv import load_dotenv
from email.header import decode_header

load_dotenv()

def decode_header_value(value):
    """Handles encoded email subjects."""
    if value is None:
        return ""
    decoded, charset = decode_header(value)[0]
    if isinstance(decoded, bytes):
        return decoded.decode(charset or "utf-8", errors="ignore")
    return decoded


def unread_email_fetcher():
    try:
        gmail_user = os.getenv("GMAIL_NAME")
        gmail_password = os.getenv("GMAIL_PASSWORD")

        if not gmail_user or not gmail_password:
            print("Missing Gmail credentials in .env file")
            return []

        print("Connecting to Gmail IMAP...")
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(gmail_user, gmail_password)
        mail.select("INBOX")

        print("Fetching Unread Emails...")
        status, search_data = mail.search(None, "(UNSEEN)")

        if status != "OK":
            print("Failed to search emails")
            return []

        email_list = []
        for num in search_data[0].split():
            _, data = mail.fetch(num, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            sender = email.utils.parseaddr(msg.get("From"))[1]
            subject = decode_header_value(msg.get("Subject"))

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition")):
                        body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        break
            else:
                try:
                    body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
                except Exception:
                    body = str(msg.get_payload())

            email_list.append({
                "Sender": sender,
                "Subject": subject,
                "Body": body
            })

            mail.store(num, "+FLAGS", "\\Seen")

        mail.logout()
        print(f"Total Unread Emails Processed: {len(email_list)}")
        return email_list

    except Exception as e:
        print(f"Error fetching emails: {str(e)}")
        return []
