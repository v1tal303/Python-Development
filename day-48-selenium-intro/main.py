from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\Development\chromedriver.exe")

browser = webdriver.Chrome(service=s)
url='https://www.python.org/'
browser.get(url)

# price = browser.find_element(By.ID,"priceblock_ourprice")
# print(price.text)


# search_bar = browser.find_element(By.NAME, "field-keywords")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = browser.find_element(By.CLASS_NAME, "nav-logo-link")
# print(logo.size)

# doc_link = browser.find_element(By.CSS_SELECTOR, "a-section")
# print(doc_link.text)

# link_byxpath = browser.find_element(By.XPATH, '//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[2]/a')
# print(link_byxpath.text)


"//*[@id='content']/div/section/div[2]/div[2]/div/ul"



event_dates = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_names[n].text,
    }

print(events)

print(event_dates)



# for i in event_dates[::2]:
#     print(i.text)

# browser.close() #Close the tab
browser.quit() #Shuts down the browser