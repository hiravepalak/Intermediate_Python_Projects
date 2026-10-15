from datetime import datetime, timedelta
import requests_cache
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

requests_cache.install_cache(
    cache_name="flight_cache",
    expire_after=3600,
    urls_expire_after={"*.sheety.co/*": 0},
)

today = datetime.now()
tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(days=180)

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

prices_list = sheet_data.get("prices", [])

customers = data_manager.get_customer_emails()
customer_email_list = [row.get("email") or row.get("Email") for row in customers if row.get("email") or row.get("Email")]

for row in prices_list:
    destination_code = row.get("iataCode")
    row_id = row.get("id")
    current_sheet_price = float(row.get("lowestPrice", 0))

    print(f"\nGetting direct flights for {destination_code}...")
    cheapest_flight = flight_search.check_flights(
        origin_city_code="LHR",
        destination_city_code=destination_code,
        from_time=tomorrow.strftime("%Y-%m-%d"),
        to_time=six_month_from_today.strftime("%Y-%m-%d"),
        is_direct=True
    )

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination_code}. Looking for indirect flights...")
        cheapest_flight = flight_search.check_flights(
            origin_city_code="LHR",
            destination_city_code=destination_code,
            from_time=tomorrow.strftime("%Y-%m-%d"),
            to_time=six_month_from_today.strftime("%Y-%m-%d"),
            is_direct=False
        )

    if cheapest_flight.price != "N/A":
        print(
            f"Lowest price found for {destination_code}: GBP {cheapest_flight.price}"
            f" (Sheet price: GBP {current_sheet_price})"
        )

        if cheapest_flight.price < current_sheet_price:
            print(f"--> Cheaper flight found! Sending notifications and updating sheet...")

            if cheapest_flight.stops == 0:
                message = (f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                           f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                           f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}.")
            else:
                message = (f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                           f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                           f"with {cheapest_flight.stops} stop(s), "
                           f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}.")

            notification_manager.send_sms(
                price=cheapest_flight.price,
                origin_airport=cheapest_flight.origin_airport,
                destination_airport=cheapest_flight.destination_airport,
                out_date=cheapest_flight.out_date,
                return_date=cheapest_flight.return_date,
            )

            if customer_email_list:
                notification_manager.send_emails(customer_email_list, message)

            data_manager.update_lowest_price(new_price=cheapest_flight.price, row_id=row_id)
        else:
            print(f"--> Price is not lower than current record. No action taken.")
    else:
        print(f"Skipping sheet update for {destination_code} (No flights available).")
