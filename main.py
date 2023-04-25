# Amazon price tracker

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib, ssl
from dotenv import load_dotenv
import os

url = os.getenv('url')
header = {
    "Accept-Language":"en-US,en;q=0.9",
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
span = soup.find("span", {"class": "a-price-whole"})
title = soup.find("span", {"class": "a-size-large product-title-word-break"})

print(title)

final_title = title.text
print(final_title)

price = ""
raw_price = span.text
# removing fullstop 
raw_price = raw_price.rstrip(raw_price[-1])
# split it by commas
price_split_array = raw_price.split(",")
# append all these in price
for price_split in price_split_array:
    price += price_split
price = float(price)
# print(price)

load_dotenv()
sender = os.getenv('sender')
password = os.getenv('password')
receiver = os.getenv('receiver')
# print(sender)

buy_price_threshold = os.env('buy_price_threshold')
buy_price_threshold = int(buy_price_threshold)

if price < buy_price_threshold:
    message = f"{final_title} is now priced at {price}! Grab the deal!"

mail_message = f"Subject:Amazon price alert.\n\n{message}\n{url}."

while True:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl.create_default_context()) as connection:
        connection.login(sender, password)
        connection.sendmail(sender,receiver, msg=mail_message)
    break
