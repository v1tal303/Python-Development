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

# TODO 1: Compare list of lowest prices to the flight prices and return flights which are cheaper

# TODO 2: Send out a txt message with the lower prices

lower_price = {}

for key in flight_data:
    if flight_data[key]["price"] < destination_lowest_price[position+1]:
        print(flight_data)

print(lower_price)
#
# flight_data = flight_data.FlightData().lowest_prices()
#
# message_text=notification_manager.NotificationManager().send_message(flight_data)
