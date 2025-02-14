import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
time.sleep(10)
links=driver.find_element(By.LINK_TEXT,"Digital downloads")
links.click()
time.sleep(2)