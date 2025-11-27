import imaplib
import email
import os
from dotenv import load_dotenv
from email.header import decode_header

load_dotenv()

def decode_header_value(value):
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
            print("Missing Gmail credentials in .env")
            return []

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(gmail_user, gmail_password)
        mail.select("INBOX")

        print("Fetching UNSEEN emails...")
        status, search_data = mail.search(None, "(UNSEEN)")

        if status != "OK" or search_data[0] == b'':
            print("⚠ No unread emails found")
            return []

        email_list = []
        for num in search_data[0].split():
            result, uid_data = mail.fetch(num, "(UID)")
            decoded_uid = uid_data[0].decode()


            import re
            uid_match = re.search(r'UID (\d+)', decoded_uid)
            uid = uid_match.group(1) if uid_match else None


            _, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            sender = email.utils.parseaddr(msg.get("From"))[1]
            subject = decode_header_value(msg.get("Subject"))

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition")):
                        body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

            email_list.append({
                "UID": uid,
                "Sender": sender,
                "Subject": subject,
                "Body": body
            })

            print(f"Found Email → UID:{uid}, Subject:{subject}")

        mail.logout()
        return email_list

    except Exception as e:
        print(f"Email fetching error: {str(e)}")
        return []
