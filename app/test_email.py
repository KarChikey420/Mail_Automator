from emial_sender import send_email
from email_reader import unread_email_fetcher

send_email("kartikeynegi2002@gmail.com", "Test Subject", "This is a test email body.")

emails = unread_email_fetcher()
print(emails)

