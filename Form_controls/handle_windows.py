import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()


windowid = driver.current_window_handle
print(windowid)

windowIDs  = driver.window_handles

parentWindow_id = windowIDs[0]
childWindow_id = windowIDs[1]

print("ParentWindowId",parentWindow_id)
print("ChildWindowId",childWindow_id)

#This is to iterate b/w multiple windows


for winId in windowIDs:
    driver.switch_to.window(winId)
    print(driver.title)                        #This prints the title of each window
    if driver.title=="OrangeHRM":
        driver.close()
