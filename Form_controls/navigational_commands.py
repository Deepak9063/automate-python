import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()

driver.refresh()
driver.close()