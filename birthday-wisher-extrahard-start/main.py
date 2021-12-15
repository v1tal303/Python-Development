import pandas
import smtplib
import datetime as dt
import os, random
from email.mime.text import MIMEText

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


# Time setup - get today's month and day

now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Birthday file setup - read file/get index of people with matching month and date/get their names

birthdays = pandas.read_csv("birthdays.csv")
index_list = birthdays[(birthdays['month'] == current_month) & (birthdays['day'] == current_day)].index.tolist()
birthday_names = birthdays.iloc[index_list]["name"]

# Send out an email - for each birthday name get a random templace/replace first line/get email as string item

for i in birthday_names:
    random_file = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{random_file}", "r") as file:
        data = file.readlines()
    data[0] = f"Dear {i}\n"
    bday_message = "".join(data)
    receiver = birthdays[birthdays["name"] == i]["email"].item()
    print(receiver)
    sendMessage(makeMessage(f"Happy Birthday {i}!", bday_message))
