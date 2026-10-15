import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("SERP_API_KEY")
        self.endpoint = "https://serpapi.com/search"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "stops": "0" if is_direct else "1,2",
            "api_key": self.api_key,
        }

        response = requests.get(self.endpoint, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None

        try:
            flights_list = data.get("best_flights", []) + data.get("other_flights", [])
            if not flights_list:
                return FlightData("N/A", origin_city_code, destination_city_code, from_time, to_time, 0)

            # Find the cheapest flight entry
            cheapest = float('inf')
            chosen_flight = None
            for flight in flights_list:
                price = flight.get("price")
                if price and price < cheapest:
                    cheapest = price
                    chosen_flight = flight

            if chosen_flight is None:
                return FlightData("N/A", origin_city_code, destination_city_code, from_time, to_time, 0)

            segments = chosen_flight.get("flights", [])
            nr_stops = len(segments) - 1 if segments else 0

            return FlightData(
                price=cheapest,
                origin_airport=origin_city_code,
                destination_airport=destination_city_code,
                out_date=from_time,
                return_date=to_time,
                stops=nr_stops
            )

        except (KeyError, TypeError, IndexError):
            return FlightData("N/A", origin_city_code, destination_city_code, from_time, to_time, 0)