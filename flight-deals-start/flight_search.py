import config
import requests
import data_manager

flight_ID = config.FLIGHT_ID
flight_KEY = config.FLIGHT_KEY
flight_END = config.FLIGH_ENDPOINT

flight_header = {
    "apikey": flight_KEY,
    "accept": "application/json"
}

flight_params = {
    "fly_from": "city:FRA",
    "fly_to": "city:PRG",
    "dateFrom": "17/12/2021",
    "dateTo": "18/12/2021",
}

f_city = ['Paris', 'Berlin']

city_params = {
    "term": f_city,
    "location_types": "city",
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.AITA_codes = []
        # self.sheet_data = data_manager.DataManager().get_destination_data()
        # self.list_of_cities = [i["city"] for i in self.sheet_data]
        # f_city = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco',
        #           'Cape Town']
        f_city = ['Paris', 'Berlin']
        self.codes = []


    def get_destination_code(self):
        for i in f_city:
            response = requests.get(url=f"{flight_END}/locations/query", params={"term": i, "location_types": "city", },
                                    headers=flight_header)
            self.AITA_codes = response.json()["locations"][0]["code"]
            self.codes.append(self.AITA_codes)
        return self.codes

