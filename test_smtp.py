import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()
admin_email = os.getenv("SMTP_EMAIL", "").strip()
smtp_pass = os.getenv("SMTP_PASSWORD", "").strip()

print(f"Email: '{admin_email}'")
print(f"Pass length: {len(smtp_pass)}")

try:
    print(f"Attempting login for '{admin_email}'...")
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(admin_email, smtp_pass)
        print("SUCCESS: Login Successful!")
except Exception as e:
    print(f"FAILURE: Login Failed: {str(e)}")
