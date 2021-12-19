import requests
import config
import datetime as dt
from twilio.rest import Client

auth_token = config.twilio_auth_token
account_sid = config.twilio_account_sid
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num
client = Client(account_sid, auth_token)


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
            self.price = data["price"]
            self.city_from = data["from_city"]
            self.code_from = data["from_airport"]
            self.city_to = data["to_city"]
            self.code_to = data["to_airport"]
            self.from_date = (data["when"]).split("T")[0]
            self.return_date = data["return"].split("T")[0]
            message_text = f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.code_from} to {self.city_to}-{self.code_to}, from {self.from_date} to {self.return_date}"
            message = client.messages \
                .create(
                body=message_text,
                from_=twilio_phone_number,
                to=my_phone_number
            )
            print(message_text)

        # for key in data:
        #     self.price = data[key]["price"]
        #     self.city_from = data[key]["from_city"]
        #     self.code_from = data[key]["from_airport"]
        #     self.city_to = data[key]["to_city"]
        #     self.code_to = data[key]["to_airport"]
        #     self.from_date = (data[key]["when"]).split("T")[0]
        #     self.return_date = data[key]["return"].split("T")[0]
        #     message_text = f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.code_from} to {self.city_to}-{self.code_to}, from {self.from_date} to {self.return_date}"
        #     # message = client.messages \
        #     #     .create(
        #     #     body=message_text,
        #     #     from_=twilio_phone_number,
        #     #     to=my_phone_number
        #     # )
        #     print(message_text)


