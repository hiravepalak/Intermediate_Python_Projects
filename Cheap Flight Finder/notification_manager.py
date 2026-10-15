import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.url = "https://od2.in/api/sms/send"
        self.auth = HTTPBasicAuth(
            "AC383ffcbbb3cf4534d6945a5f93525672",
            "sk_sms_09ca7febef6594598c0d475a5efc6a8e9049d19a4d1570a8",
        )

        self.smtp_address = os.getenv("SMTP_ADDRESS")
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")

    def send_sms(
            self, price, origin_airport, destination_airport, out_date, return_date
    ):
        message_body = (
            f"Low price alert! Only GBP {price} to fly "
            f"from {origin_airport} to {destination_airport}, "
            f"from {out_date} to {return_date}."
        )

        payload = {
            "from": "+15551234567",
            "to": "+18005550199",
            "body": message_body,
        }

        response = requests.post(self.url, json=payload, auth=self.auth)
        print("SMS Notification Response:", response.json())

    def send_emails(self, email_list, message_body):
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for email in email_list:
                msg = MIMEMultipart()
                msg['From'] = self.email
                msg['To'] = email
                msg['Subject'] = "New Low Price Flight Deal!"

                # Attach message with UTF-8 encoding to support characters safely
                msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=msg.as_string()
                )
        print("Emails sent successfully to all customers.")