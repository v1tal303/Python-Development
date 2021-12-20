from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time
import random

s = Service("C:\Development\chromedriver.exe")

browser = webdriver.Chrome(service=s)
url = 'https://orteil.dashnet.org/cookieclicker/'
browser.get(url)

end = time() + 3000
upgrade_time = time() + 5
cookies_persecond = ""

# Run the script for {end} minutes

while True:
    if time() > end:
        break
    cookie_count_html = browser.find_element(By.ID, "cookies")
    cookie_button = browser.find_element(By.CSS_SELECTOR, "#bigCookie")
    cookie_button.click()
    cookie_count = cookie_count_html.text.split()[0]
    cookies_persecond = cookie_count_html.text.split()[5]
    products = browser.find_elements(By.CSS_SELECTOR, ".enabled")[-1]
    try:
        if time() > upgrade_time:
            randomize = random.randint(0, 1)
            print(randomize)
            if randomize == 0:
                upgrades = browser.find_elements(By.CSS_SELECTOR, ".upgrade.enabled")[-1]
                upgrades.click()
                print("PURCHASED AN UPGRADE")
            else:
                products.click()
                print("PURCHASED A PRODUCT")
            upgrade_time = time() + 5
    except:
        pass

print(f"YOUR COOKIES PER SECOND VALUE IS: {cookies_persecond}")
