from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time, sleep
import config

TWITTER_EMAIL = config.TWITTER_EMAIL
TWITTER_PASSWORD = config.TWITTER_PASSWORD

class InternetSpeedBot:

    def __init__(self):
        s = Service("C:\Development\chromedriver.exe")
        self.down = 0
        self.up = 0
        self.browser = webdriver.Chrome(service=s)
        self.url = ""

    def get_internet_speed(self):
        self.url = "https://www.speedtest.net/"
        self.browser.get(self.url)
        sleep(5)
        consent_button = self.browser.find_element(By.XPATH, "//*[@id='_evidon-banner-acceptbutton']")
        consent_button.click()
        start_button = self.browser.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        start_button.click()
        sleep(60)
        self.down = float(self.browser.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)
        self.up = float(self.browser.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text)
        print(self.down)
        print(self.up)
        return {"Download": self.down,
                "Upload": self.up,
                }

    def tweet_at_provider(self):
        self.url = "https://twitter.com/home"
        self.browser.get(self.url)
        sleep(5)
        email_login = self.browser.find_element(By.NAME, "text")
        email_login.send_keys(TWITTER_EMAIL)
        email_next = self.browser.find_element(By.CSS_SELECTOR, ".css-18t94o4.r-13qz1uu")
        email_next.click()
        sleep(5)
        try:
            phone_login = self.browser.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            phone_login.send_keys("test")
            phone_next = self.browser.find_element(By.CSS_SELECTOR, ".css-18t94o4.r-lrvibr")
            phone_next.click()
        except:
            password_login = self.browser.find_element(By.NAME, "")
            password_login.send_keys(TWITTER_PASSWORD)

        ## TBC. Need to fix the login/bot issue