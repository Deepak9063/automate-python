import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()
time.sleep(3)
visa_options = driver.find_elements(By.XPATH,"//ul[@id='select2-reasondummy-results']/li")
print(len(visa_options))

for option in visa_options:
    print(option.text)
    if option.text=="Proof of return at airport":
        option.click()
        break

time.sleep(5)
