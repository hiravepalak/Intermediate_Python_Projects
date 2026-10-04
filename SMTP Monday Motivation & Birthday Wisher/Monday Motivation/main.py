import smtplib
import datetime as dt
import random

MY_GMAIL = "fake_sender@gmail.com"
FAKE_PASSWORD = "any_password_works"
RECEIVER_YAHOO = "fake_receiver@yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('quotes.txt') as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("localhost", port=1025) as connection:
        connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=MY_GMAIL,
                msg=f"This is your weekly monday quote!\n \n{quote}"
            )

