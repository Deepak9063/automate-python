import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()

driver.get("https://total-qa.com/checkbox-example/#google_vignette")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for i in range(len(checkboxes)):
    checkboxes[i].click()
    #or

# for checkbox in checkboxes:
#     checkbox.click()

time.sleep(4)