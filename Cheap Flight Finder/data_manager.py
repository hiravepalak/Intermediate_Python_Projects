import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.sheety_prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.sheety_users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.sheety_username = os.getenv("SHEETY_USERNAME")
        self.sheety_password = os.getenv("SHEETY_PASSWORD")

        # Setup authentication (using Bearer token or HTTPBasicAuth depending on your Sheety setup)
        self.auth_head = {"Authorization": f"Bearer {os.getenv('AUTH_TOKEN') or ''}"}

    def get_data(self):
        response = requests.get(self.sheety_prices_endpoint, headers=self.auth_head)
        return response.json()

    def get_customer_emails(self):
        response = requests.get(self.sheety_users_endpoint, headers=self.auth_head)
        data = response.json()
        # Adjust "users" based on the sheet name in your Google Sheets
        users = data.get("users", [])
        return users

    def update_lowest_price(self, new_price, row_id):
        print(requests.put(f"{self.sheety_prices_endpoint}/{row_id}", headers=self.auth_head,
                           json={"price": {"lowestPrice": new_price}}))

