import smtplib
import datetime as dt
import random
import pandas as pd

MY_GMAIL = "fake_sender@gmail.com"
FAKE_PASSWORD = "any_password_works"
RECEIVER_YAHOO = "fake_receiver@yahoo.com"

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row
    for (index, data_row) in data.iterrows()
}

if today in birthdays_dict:
    letters = ('letter_1.txt', 'letter_2.txt', 'letter_3.txt')
    chosen_letter = random.choice(letters)
    birthday_person = birthdays_dict[today]
    person_name = birthday_person["name"]
    with open(f'letter_templates/{chosen_letter}', 'r') as file:
        letter_contents = file.read()
    customized_letter = letter_contents.replace('[NAME]', person_name)


    with smtplib.SMTP("localhost", port=1025) as connection:
        connection.sendmail(
                    from_addr=MY_GMAIL,
                    to_addrs=RECEIVER_YAHOO,
                    msg=f"Subject: Happy Birthday!\n{customized_letter}"
                 )