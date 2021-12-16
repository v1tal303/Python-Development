import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import config

my_lat = config.my_lat
my_lon = config.my_lon
api_key = config.OWM_api_key
exclusions = "current,minutely,daily"

#Twilio
auth_token = config.twilio_auth_token
account_sid = config.twilio_account_sid
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num



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

will_rain = False

for i in list_of_id:
    if i < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_=twilio_phone_number,
        to=my_phone_number
    )
    print(message.status)