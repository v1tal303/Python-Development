import datetime as dt
import requests
import config
import flight_search

flight_ID = config.FLIGHT_ID
flight_KEY = config.FLIGHT_KEY
flight_END = config.FLIGH_ENDPOINT

flight_params = {
    "fly_from": "LON",
    "fly_to": "PAR",
    "dateFrom": "17/12/2021",
    "dateTo": "18/12/2021",
}

flight_header = {
    "apikey": flight_KEY,
    "accept": "application/json"
}


class FlightData:

    def __init__(self):
        self.now = dt.date.today()
        self.today = self.now.strftime("%d/%m/%Y")
        self.future = (self.now + dt.timedelta(days=6 * 30)).strftime("%d/%m/%Y")
        self.flight_params = {}
        # self.codes = flight_search.FlightSearch().get_destination_code()
        self.flight_info = {}


    def lowest_prices(self, codes):
        for i in codes:
            self.flight_params = {
                "fly_from": "LON",
                "fly_to": i,
                "dateFrom": self.today,
                "dateTo": self.future,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "curr": "GBP",
            }
            response = requests.get(url=f"{flight_END}/v2/search", params=self.flight_params, headers=flight_header)
            flight_data = response.json()
            lowest_price = flight_data["data"][0]["price"]
            fly_from = flight_data["data"][0]["flyFrom"]
            from_city = flight_data["data"][0]["route"][0]["cityFrom"]
            fly_to = flight_data["data"][0]["flyTo"]
            to_city = flight_data["data"][0]["route"][1]["cityFrom"]
            departure_time = flight_data["data"][0]["route"][0]["local_departure"]
            return_time = flight_data["data"][0]["route"][1]["local_departure"]
            self.flight_info.update({i: {"price": lowest_price,
                                         "from_airport": fly_from,
                                         "from_city": from_city,
                                         "to_airport": fly_to,
                                         "to_city": to_city,
                                         "when": departure_time,
                                         "return": return_time, }})
            print(f"The price for destination {i} is {lowest_price}")
        print(self.flight_info)
        return self.flight_info
