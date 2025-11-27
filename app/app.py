from flask import Flask, jsonify, request
from flask_cors import CORS
from email_reader import unread_email_fetcher
from emial_sender import send_email
from rag_engine import generte_response
from spam_or_not import spam_or_not
from chroma_db import store_emails_in_vector_db
import imaplib, os

app = Flask(__name__)
CORS(app)

pending_emails = []

@app.route('/process_emails', methods=["GET"])
def process_emails():
    global pending_emails
    pending_emails = []

    emails = unread_email_fetcher()
    if not emails:
        return jsonify({"message": "No new emails found"}), 200

    filtered_emails = []
    for email_data in emails:
        if not spam_or_not(email_data["Body"]):
            pending_emails.append(email_data)
            filtered_emails.append({
                "email": email_data["Subject"],
                "sender": email_data["Sender"],
                "index": len(pending_emails) - 1,
                "uid": email_data["UID"],
                "status": "Not Spam",
                "can_process": True
            })

    return jsonify({"pending_emails": filtered_emails}), 200

@app.route('/process_single_email', methods=["POST"])
def process_single_email():
    global pending_emails
    try:
        email_index = request.json.get("index")
        email_uid = request.json.get("uid")
        print(f"Processing email at index: {email_index} with UID: {email_uid}")

        if email_index is None:
            return jsonify({"error": "Email index not provided"}), 400
            
        if len(pending_emails) == 0:
            return jsonify({"error": "No emails available to process"}), 400
            
        if email_index >= len(pending_emails):
            return jsonify({"error": "Invalid email selection"}), 400

        email_data = pending_emails[email_index]
        reply_text, _ = generte_response(email_data)
        subject = f"Re: {email_data['Subject']}"

        send_status = send_email(email_data["Sender"], subject, reply_text)
        store_emails_in_vector_db([email_data])
        pending_emails.pop(email_index)

        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(os.getenv("GMAIL_NAME"), os.getenv("GMAIL_PASSWORD"))
            mail.select("INBOX")
            if email_uid:
                mail.uid('STORE', email_uid, '+FLAGS', '(\\Seen)')
                print(f"Marked email UID {email_uid} as seen")
            mail.logout()
        except Exception as mark_error:
            print(f"Could not mark email as read: {mark_error}")

        return jsonify({
            "email": email_data["Subject"],
            "sender": email_data["Sender"],
            "status": "Reply Sent" if send_status else "Reply Failed",
            "reply": reply_text
        }), 200

    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
