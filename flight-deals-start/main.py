import config
import requests
from pprint import pprint
import data_manager
import flight_search
import flight_data
import notification_manager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

codes = ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']

sheet_data = data_manager.DataManager().get_destination_data()
destination_cities = []
destination_lowest_price = []
position = -1
print(sheet_data)

for i in sheet_data:
    destination_cities.append(sheet_data[sheet_data.index(i)]["city"])
    destination_lowest_price.append(sheet_data[sheet_data.index(i)]["lowestPrice"])
print(destination_cities)
print(destination_lowest_price)

destination_codes = flight_search.FlightSearch().get_destination_code(destination_cities)

print(destination_codes)

flight_data = flight_data.FlightData().lowest_prices(destination_codes)

print(flight_data)
print(sheet_data)

# # TODO 1: Compare list of lowest prices to the flight prices and return flights which are cheaper
#
# # TODO 2: Send out a txt message with the lower prices
# ------------
lower_price = {}

# test1 = {'PAR': {'price': 58, 'from_airport': 'LGW', 'from_city': 'London', 'to_airport': 'CDG', 'to_city': 'Paris', 'when': '2022-05-11T07:50:00.000Z', 'return': '2022-06-02T07:00:00.000Z'}, 'BER': {'price': 34, 'from_airport': 'STN', 'from_city': 'London', 'to_airport': 'BER', 'to_city': 'Berlin', 'when': '2022-01-08T07:20:00.000Z', 'return': '2022-01-18T19:45:00.000Z'}, 'TYO': {'price': 585, 'from_airport': 'STN', 'from_city': 'London', 'to_airport': 'HND', 'to_city': 'Tallinn', 'when': '2022-01-28T05:55:00.000Z', 'return': '2022-01-28T18:40:00.000Z'}, 'SYD': {'price': 601, 'from_airport': 'STN', 'from_city': 'London', 'to_airport': 'SYD', 'to_city': 'Berlin', 'when': '2022-01-18T19:05:00.000Z', 'return': '2022-01-19T10:45:00.000Z'}, 'IST': {'price': 80, 'from_airport': 'STN', 'from_city': 'London', 'to_airport': 'SAW', 'to_city': 'Istanbul', 'when': '2022-03-21T15:35:00.000Z', 'return': '2022-04-01T08:45:00.000Z'}, 'KUL': {'price': 505, 'from_airport': 'STN', 'from_city': 'London', 'to_airport': 'KUL', 'to_city': 'Milan', 'when': '2022-01-19T08:45:00.000Z', 'return': '2022-01-19T15:50:00.000Z'}, 'NYC': {'price': 286, 'from_airport': 'LHR', 'from_city': 'London', 'to_airport': 'JFK', 'to_city': 'Lisbon', 'when': '2022-01-29T13:40:00.000Z', 'return': '2022-01-30T17:00:00.000Z'}, 'SFO': {'price': 321, 'from_airport': 'LHR', 'from_city': 'London', 'to_airport': 'SFO', 'to_city': 'Frankfurt', 'when': '2022-01-24T08:30:00.000Z', 'return': '2022-01-24T12:50:00.000Z'}, 'CPT': {'price': 400, 'from_airport': 'LHR', 'from_city': 'London', 'to_airport': 'CPT', 'to_city': 'Munich', 'when': '2022-01-09T13:50:00.000Z', 'return': '2022-01-09T17:45:00.000Z'}}
#
# required_prices = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]


current_prices = []


for i in flight_data:
    current_prices.append(flight_data[i])


# flight_data = flight_data.FlightData().lowest_prices()
#
# message_text=notification_manager.NotificationManager().send_message(flight_data)

for a, b in zip(current_prices, sheet_data):
    if a["price"] < b["lowestPrice"]:
        message_text=notification_manager.NotificationManager().send_message(a)