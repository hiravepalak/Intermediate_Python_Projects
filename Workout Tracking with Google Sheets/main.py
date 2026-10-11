import requests
import os
import datetime

from dotenv import load_dotenv
load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT_KG = int(os.getenv("WEIGHT_KG") or 1)
HEIGHT_CM = int(os.getenv("HEIGHT_CM") or 1)
AGE = int(os.getenv("AGE") or 1)

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

# Source : https://app.100daysofpython.dev/dashboard?verified=true
BACE_ENDPOINT = "https://app.100daysofpython.dev"
exercise_text = input("Tell me which exercises you did: ")

headers = {"x-app-id": os.getenv("APP_ID"),
           "x-app-key": os.getenv("API_KEY")}

parameters = {"query": exercise_text,
              "gender": GENDER,
              "weight_kg": WEIGHT_KG,
              "height_cm": HEIGHT_CM,
              "age": AGE}

response = requests.post(f"{BACE_ENDPOINT}/v1/nutrition/natural/exercise", json=parameters, headers=headers)
data = response.json()

SHEETY_ENDPOINT = f"https://api.sheety.co/{os.getenv("SHEETY_USERNAME") or ""}/myWorkouts(day38Python)/workouts"

exercise = data["exercises"][0]["name"].title()
sheety_tabs = {"workout": {
    "date": datetime.date.today().strftime("%d/%m/%Y"),
    "time": str(datetime.datetime.now().time())[:8],  # Also fixed to use actual current time
    "exercise": exercise,
    "duration": data["exercises"][0]["duration_min"],
    "calories": data["exercises"][0]["nf_calories"]}
    }

auth_head = {"Authorization": f"Bearer {os.getenv('AUTH_TOKEN')}"}

requests.post(SHEETY_ENDPOINT, json=sheety_tabs, headers=auth_head)




