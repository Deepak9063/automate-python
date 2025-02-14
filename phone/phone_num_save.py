import time

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    "platformName" : "Android",
    "deviceName" : "emulator-5554",
    "automationName" : "uiAutomator2",
    "appPackage" : "com.google.android.dialer",
    "appActivity" : "com.android.dialer.main.impl.MainActivity"

}

url = "http://localhost:4723/wd/hub"

driver = webdriver.Remote(url,desired_capabilities=desired_cap)
contacts_button = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Contacts']")
contacts_button.click()
time.sleep(3)
create_contact = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Create new contact']")
create_contact.click()
time.sleep(4)

first_name = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='First name']")
first_name.send_keys("Shashank")

last_name = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Last name']")
last_name.send_keys("L")

#using drop downs
dropdown = driver.find_element(AppiumBy.XPATH,"//android.widget.Spinner[@text='Mobile']")
dropdown.click()
time.sleep(10)

options = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Spinner")
time.sleep(4)
for ele in options:
    print(ele.text)
    if ele.text=="Home":
        ele.click()

allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

time.sleep(3)

# save_button = driver.find_element(AppiumBy.XPATH,"//android.
# widget.Button[@text='Save']")
# save_button.click()


