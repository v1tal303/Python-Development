import requests
from datetime import datetime

MY_LAT = 52.435928
MY_LNG = -2.086180

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data = response.json()
#
# print(data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


time_now = datetime.now()

print(time_now.hour)