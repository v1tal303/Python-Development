import requests
import config
import datetime as dt


class NotificationManager:


    def __init__(self):
        self.price = 0
        self.city_from = ""
        self.code_from = ""
        self.city_to = ""
        self.code_to = ""
        self.from_date = ""
        self.return_date = ""

    def send_message(self, data):

        for key in data:
            self.price = data[key]["price"]
            self.city_from = data[key]["from_city"]
            self.code_from = data[key]["from_airport"]
            self.city_to = data[key]["to_city"]
            self.code_to = data[key]["to_airport"]
            self.from_date = (data[key]["when"]).split("T")[0]
            self.return_date = data[key]["return"].split("T")[0]
            message = f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.code_from} to {self.city_to}-{self.code_to}, from {self.from_date} to {self.return_date}"
            print(message)
