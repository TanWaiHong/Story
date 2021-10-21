from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "KUL"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only RM{flight.price} " \
                  f"to fly from {flight.origin_city}-" \
                  f"{flight.origin_airport} to " \
                  f"{flight.destination_city}-" \
                  f"{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, " \
                       f"via {flight.via_city}."

        notification_manager.send_sms(message)
