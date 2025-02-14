import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.nopcommerce.com/login")
time.sleep(3)

button = driver.find_element(By.XPATH,"//input[@value='Log in']")
print("Result of text",button.text)
print("get_attribute():",button.get_attribute('value'))