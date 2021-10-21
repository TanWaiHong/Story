import requests
import os


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.city_codes = None

    def get_destination_data(self):
        header = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
        }
        response = requests.get(
            url=os.getenv('SHEETY_END_POINT'),
            headers=header
        )
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for code in self.city_codes:
            new_data = {
                "price": {
                    "iataCode": code
                }
            }

            header = {
                "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
            }

            response = requests.put(
                url=f"{os.getenv('SHEETY_END_POINT')}/{self.city_codes.index(code) + 2}",
                json=new_data,
                headers=header
            )
            print(response.text)

