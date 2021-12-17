import requests
import config
import flight_search


# SHEETY API

SHEETY_KEY = config.SHEETY_KEY
SHEETY_PROJECT = "flightDeals"
SHEETY_SHEET = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_KEY}/{SHEETY_PROJECT}/{SHEETY_SHEET}"
SHEETY_AUTH = config.SHEETY_AUTH

sheety_header = {
    "Content-Type": "application/json",
}

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.flight_search = flight_search.FlightSearch()
        self.destination_code = {}


    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        self.destination_code = self.flight_search.get_destination_code()
        for i in self.destination_code:
            new_data = {
                "price": {
                    "iataCode": i
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{self.destination_code.index(i)+2}", json=new_data)

