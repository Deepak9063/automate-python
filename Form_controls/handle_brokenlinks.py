import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_element(By.TAG_NAME,"a")
time.sleep(5)
print(allLinks.text)
time.sleep(10)
count = 0

for link in allLinks:
    url = link.get_attribute("href")
    try:
        res = requests.get(url)
    except:
        None

    if res.status_code>=400:
        print(url,"It is a broken link")
        count += 1
    else:
        print(url,"It is a broken link")

print("Total number of broken links are",count)


