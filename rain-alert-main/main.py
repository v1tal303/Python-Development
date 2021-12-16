import requests

my_lat = 52.486244
my_lon = -1.890401
api_key = "9f83d4d2dda67c80b05482e5cc252eb2"
exclusions = "current,minutely,daily"

parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "exclude": exclusions,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# list_of_id = []
# for i in weather_data["hourly"][:12]:
#     list_of_id.append(i["weather"][0]["id"])

list_of_id = [i["weather"][0]["id"] for i in weather_data["hourly"][:12]]

print(list_of_id)

for i in list_of_id:
    if i < 700:
        print("Bring an umbrella")