import requests
from requests.auth import HTTPBasicAuth

api_key ='ab560967bb3ce640fa05fd409bc69545'

params = {'lat': 13.7563,
          'lon': 100.5018,
          'appid': api_key,
          'cnt': 4}
response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params)
response.raise_for_status()
weather_data = response.json()

ids = []
for num in range(0,4):
        condition = weather_data['list'][num]['weather'][0]['id']
        ids.append(condition)

is_raining = False
for id in ids:
        if id < 700:
            is_raining = True

if is_raining:
    url = "https://od2.in/api/sms/send"
    auth = HTTPBasicAuth("AC585e41e0a9bda98b9ead84ccfb25b535",
                         "sk_sms_585f98adcabaf49d1589a3dd63a50757b1e338e4fcd82466")
    payload = {
        "from": "+15551234567",
        "to": "+907796536851",
        "body": "It is Raining Today! Make sure to bring an umbrella!."
    }

    response = requests.post(url, json=payload, auth=auth)
    print(response.json())
