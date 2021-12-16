import requests
from datetime import datetime
import config

pixela_endpoint = config.pixela_endpoint
USERNAME = config.USERNAME
TOKEN = config.TOKEN

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
graps_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graps_config, headers=headers)
#
# print(response.text)
#
add_gvalue = f"{pixela_endpoint}/{USERNAME}/graphs/{graps_config['id']}"

today = datetime.now()
today_str = today.strftime("%Y%m%d")

print(today_str)

gvalue_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.3",
}

# response = requests.post(url=add_gvalue, json=gvalue_config, headers=headers)
# print(response.text)

update_config = {
    "quantity": "4",
}

update_url = f"{pixela_endpoint}/{USERNAME}/graphs/{graps_config['id']}/{today_str}"

# response = requests.put(url=update_url, json=update_config, headers=headers)


## DELETE method
response = requests.delete(url=update_url, headers=headers)
print(response.text)