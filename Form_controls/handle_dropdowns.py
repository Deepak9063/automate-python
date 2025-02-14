import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
#We have used the Select method to selct b/w the dropdowns
drp_option = Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))

drp_option.select_by_visible_text("Option1")
time.sleep(3)
#we can do this by select by value also
#drp_option.select_by_value("10")

all_options = drp_option.options
print(len(all_options))

for opt in all_options:
    print(opt.text)

time.sleep(5)
