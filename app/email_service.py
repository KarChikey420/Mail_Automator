from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_services():
    cred=None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            cred=pickle.load(token)
    
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow=InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            cred=flow.run_local_server(port=0)
            
        with open("token.pickle","wb") as token:
            pickle.dump(cred, token)
    return build("gmail","v1",credentials=cred)