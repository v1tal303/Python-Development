import config
import requests
from pprint import pprint
import data_manager
import flight_search
import flight_data
import notification_manager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


# sheet_data = data_manager.DataManager().get_destination_data()
# print(sheet_data)


# flight_search = flight_search.FlightSearch()
# destination_code = flight_search.get_destination_code()

#
# sheets = data_manager.DataManager()
# sheets.update_destination_codes()
#
codes = ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']



flight_ID = config.FLIGHT_ID
flight_KEY = config.FLIGHT_KEY
flight_END = config.FLIGH_ENDPOINT

flight_header = {
    "apikey": flight_KEY,
    "accept": "application/json"
}

flight_params = {
    "fly_from": "LON",
    "fly_to": "PAR",
    "dateFrom": "17/12/2021",
    "dateTo": "15/06/2022",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "curr": "GBP",
}

# response = requests.get(url=f"{flight_END}/v2/search", params=flight_params, headers=flight_header)
#
# flight_data = response.json()

# response = requests.get(url=f"{flight_END}/v2/search", params=flight_params, headers=flight_header)
#
#
# data = response.text
#
# f = open("text.txt", "w")
# f.write(data)
# f.close()
# print(response.text)

# for i in codes:
#     flight_params = {
#         "fly_from": "LON",
#         "fly_to": i,
#         "dateFrom": "17/12/2021",
#         "dateTo": "18/12/2021",
#     }
#     response = requests.get(url=f"{flight_END}/v2/search", params=flight_params, headers=flight_header)
#     flight_data = response.json()
#     lowest_price = flight_data["data"][0]["price"]
#
#     print(f"The price for destination {i} is {lowest_price}")
#
#
#
flight_data = flight_data.FlightData().lowest_prices()

message_text=notification_manager.NotificationManager().send_message(flight_data)