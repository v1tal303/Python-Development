import requests
from bs4 import BeautifulSoup
import config
from twilio.rest import Client

auth_token = config.twilio_auth_token
account_sid = config.twilio_account_sid
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num
client = Client(account_sid, auth_token)


response = requests.get(f"https://www.amazon.co.uk/Oculus-Quest-Advanced-All-One/dp/B0973RP7H3/ref=sr_1_3?crid=38YBUXLXB2BNO&keywords=oculus&qid=1640018155&sprefix=oculus%2Caps%2C72&sr=8-3", headers={"Accept-Language":"en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})

data = response.text

soup = BeautifulSoup(data, "html.parser")

price = float(soup.find(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()[1:])

item = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()

print(item)

if price < 300:
    message_text = f"Low price alert! Only £{price} for '{item}. Buy now!'"
    message = client.messages \
        .create(
        body=message_text,
        from_=twilio_phone_number,
        to=my_phone_number
    )
