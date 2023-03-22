from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

email_sender = os.getenv("EMAIL_ADDR")
email_password = os.getenv("EMAIL_APP_PASSWORD")

print(email_sender)