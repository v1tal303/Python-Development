from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:\Development\chromedriver.exe")

browser = webdriver.Chrome(service=s)
url='http://secure-retreat-92358.herokuapp.com/'
browser.get(url)

# no_articles = browser.find_element(By.CSS_SELECTOR, "#articlecount a") # #for ID, and .for classes
# no_articles.click()

# all_portals = browser.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

f_name = browser.find_element(By.NAME, "fName")
f_name.send_keys("Python")

l_name = browser.find_element(By.NAME, "lName")
l_name.send_keys("Developer")

email = browser.find_element(By.NAME, "email")
email.send_keys("Python@Developer.com")

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
