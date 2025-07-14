# test_send.py
from email_notification import send_email

send_email(
    subject="Test Email",
    content="This is a test from automation",
    to_emails=["sandun@seamlesssource.com"]
)
