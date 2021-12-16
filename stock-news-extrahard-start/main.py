import requests
import config
import datetime as dt
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

### SMS SENDING FEATURE ONLY WORKS WITH PYTHONANYWHERE.COM

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Twilio
auth_token = config.twilio_auth_token
account_sid = config.twilio_account_sid
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": config.alpha_KEY,
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Use datetime to figure out yesterday and day before yesterday as a string

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
day_before_yesterday = today - dt.timedelta(days=2)
day_before_str = day_before_yesterday.strftime("%Y-%m-%d")

yesterday_price = float(stock_data["Time Series (Daily)"][yesterday_str]["1. open"])
before_yesterday_price = float(stock_data["Time Series (Daily)"][day_before_str]["1. open"])
percentage_change = round((yesterday_price - before_yesterday_price) / before_yesterday_price * 100, 2)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "apikey": config.news_API,
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

print(news_data["articles"][:3])

article_title = [i["title"] for i in news_data["articles"][:3]]
article_brief = [i["description"] for i in news_data["articles"][:3]]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

def generate_message():
    if percentage_change > 0:
        return f"""TSLA: 🔺{percentage_change}%
        Headline: {article_title[0]}.
        Brief: {article_brief[0]}
        Headline: {article_title[1]}.
        Brief: {article_brief[1]}
        Headline: {article_title[2]}.
        Brief: {article_brief[2]}"""

    else:
        return f"""TSLA: 🔻{percentage_change}%
        Headline: {article_title[0]}.
        Brief: {article_brief[0]}
        Headline: {article_title[1]}.
        Brief: {article_brief[1]}
        Headline: {article_title[2]}.
        Brief: {article_brief[2]}"""

def send_text_message():
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=generate_message(),
        from_=twilio_phone_number,
        to=my_phone_number
    )

send_text_message()

