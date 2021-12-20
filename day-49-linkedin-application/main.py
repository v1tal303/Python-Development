from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
from time import time, sleep

s = Service("C:\Development\chromedriver.exe")

email_ID = config.email
password_ID = config.password

browser = webdriver.Chrome(service=s)
url = 'JOB URL'
browser.get(url)

signin_button = browser.find_element(By.CSS_SELECTOR, ".nav__cta-container .nav__button-secondary")
signin_button.click()

sleep(5)

email = browser.find_element(By.ID, "username")
email.send_keys(email_ID)

password = browser.find_element(By.ID, "password")
password.send_keys(password_ID)

sleep(5)

login_button = browser.find_element(By.CSS_SELECTOR, ".btn__primary--large")
login_button.click()

## This is unfinished due to missing practice job application

