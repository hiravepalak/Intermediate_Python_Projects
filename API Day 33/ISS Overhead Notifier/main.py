import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.520430
MY_LONG = 73.856743

MY_GMAIL = "fake_sender@gmail.com"
FAKE_PASSWORD = "any_password_works"
RECEIVER_YAHOO = "fake_receiver@yahoo.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def check_pos():
    lat_upper= float(MY_LAT + 5)
    lat_lower = float(MY_LAT - 5)

    long_upper = float(MY_LONG + 5)
    long_lower = float(MY_LONG - 5)

    if iss_latitude > lat_lower and iss_latitude < lat_upper:
        if iss_longitude > long_lower and iss_longitude < long_upper:
            return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    if check_pos():
        if time_now.hour >= sunset and time_now.hour <= sunrise:
            with smtplib.SMTP("localhost", port=1025) as connection:
                connection.sendmail(
                    from_addr=MY_GMAIL,
                    to_addrs=MY_GMAIL,
                    msg=f"Subject: Look Up!\nISS Is Close!"
                )

    time.sleep(60)
