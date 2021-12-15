import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time

# Default email setup - specific for mailtrap.io due to MIMEtext setup

port = 2525
smtp_server = "smtp.mailtrap.io"
login = "login"
password = "password"

sender = "from@smtp.mailtrap.io"
receiver = "to@smtp.mailtrap.io"

# Email class setup

def makeMessage(subject, content):
    message = MIMEText(content)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    return message


def sendMessage(message):
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, message.as_string())


MY_LAT = # Your latitude
MY_LONG = # Your longitude


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def is_dark():
    if not sunset <= time_now.hour <= sunrise:
        return True
    else:
        return False


def is_above():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5 and is_dark():
        print("IT IS ABOVE!")
        sendMessage(makeMessage("ISS IS ABOVE!", "Look up the iss is above"))
        return True
    else:
        print("Not above")
        return False

while True:
    time.sleep(10)
    print("The current ISS status is:")
    is_above()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



