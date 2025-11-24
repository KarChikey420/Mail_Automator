from flask import Flask, jsonify
from flask_cors import CORS
from email_reader import unread_email_fetcher
from emial_sender import send_email
from rag_engine import generte_response
from spam_or_not import spam_or_not
from chroma_db import store_emails_in_vector_db

app = Flask(__name__)
CORS(app)

@app.route('/process_emails',methods=["GET"])
def process_emails():
    try:
        emails=unread_email_fetcher()
        
        if not emails:
            return jsonify({"message":"No new emails found"}),200
        
        response=[]
        non_spam_emails=[]
        
        for email_data in emails:
            if spam_or_not(email_data["Body"]):
                response.append({
                    "email":email_data["Subject"],
                    "sender":email_data["Sender"],
                    "status":"Spam"
                })
                continue
            
            non_spam_emails.append(email_data)
            reply_text,status=generte_response(email_data)
            response.append({
                "to_email":email_data['Sender'],
                "subject": f"Re:{email_data['Subject']}",
                "reply":reply_text
            })
            
            response.append({
                "email":email_data["Subject"],
                "sender":email_data["Sender"],
                "status":"reply sent" if status else "reply failed",
                "reply":reply_text
            })
            
        if non_spam_emails:
            store_emails_in_vector_db(non_spam_emails)
        return jsonify({"processed_emails":response}),200
    except Exception as e:
        return jsonify({"error":str(e)}),500

@app.route('/get-emails',methods=["GET"])
def get_emails():
    try:
        emails=unread_email_fetcher()
        return jsonify({"emails":emails}),200
    except Exception as e:
        return jsonify({"error":str(e)}),500
    
