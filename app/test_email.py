from email_service import get_gmail_services

def test_auth():
    service=get_gmail_services()
    print("success")

test_auth()