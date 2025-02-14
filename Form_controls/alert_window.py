import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

driver.find_element(By.XPATH,"//input[@id='promptexample']").click()

alert_window = driver.switch_to.alert
time.sleep(2)

print(alert_window.text)
alert_window.send_keys("o")
time.sleep(2)
alert_window.accept()
time.sleep(4)

