import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

# if we want to scroll down upto 3000 pixels we use this
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number pixels moved",value)

# If we want to scroll upto whichever element we want we use this
# flag = driver.find_element(By.XPATH,"//img[@src='/img/flags/small/tn_in-flag.gif']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved",value)
# time.sleep(5)

#To scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
