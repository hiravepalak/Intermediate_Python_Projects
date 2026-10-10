import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params = {'apikey': os.getenv('ALPHA_VANTAGE_API_KEY'),
          'function': 'TIME_SERIES_DAILY',
          'symbol': STOCK_NAME,}

stock_get = requests.get(STOCK_ENDPOINT, params=params)
stock_data = stock_get.json()

yesterday_price = stock_data['Time Series (Daily)']['2026-10-09']['4. close']
day_before_yesterday_price = stock_data['Time Series (Daily)']['2026-10-08']['4. close']

positive_difference = abs(float(yesterday_price) - float(day_before_yesterday_price))
average = (float(yesterday_price) + float(day_before_yesterday_price))/2
percentage_difference = (positive_difference/average)*100

actual_diff = float(yesterday_price) - float(day_before_yesterday_price)

if percentage_difference > 5:

    news_params = {'language': 'en',
                    'sortBY': 'publishedAt',
                    'pageSize': 3,
                    'q': COMPANY_NAME,
                   'apiKey': os.getenv('NEWS_API_KEY')}

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()

    contents = [article["content"] for article in news_data["articles"]]
    headline = [article["title"] for article in news_data["articles"]]

    url = "https://od2.in/api/sms/send"
    auth = HTTPBasicAuth("AC1c001b95cf732537c0aa0ec671119042",
                         "sk_sms_4b32557dd6648072d10ed1d279b9b2e8c2c6b927980496d0")
    payload = {
        "from": "+15551234567",
        "to": "+18005550199",
        "body": f"STOCK CHANGED BY : {round(actual_diff, 2)}"
                f"{headline[0]}"
                f"{contents[0]}"
                f"{headline[1]}"
                f"{contents[1]}"
                f"{headline[2]}"
                f"{contents[2]}",
    }

    response = requests.post(url, json=payload, auth=auth)
    print(response.json())

