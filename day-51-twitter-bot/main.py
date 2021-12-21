from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import config
import internetspeedbot

internetspeedbot = internetspeedbot.InternetSpeedBot()

print(internetspeedbot.get_internet_speed())

internetspeedbot.tweet_at_provider()