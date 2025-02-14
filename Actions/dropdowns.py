import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}
url = "http://localhost:4723/wd/hub"
driver = webdriver.Remote(url,desired_capabilities=des_cap)
time.sleep(3)

skip_button = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Skip']")
skip_button.click()
driver.switch_to.alert.accept()
time.sleep(3)
plus_button = driver.find_element(AppiumBy.ID,"com.google.android.contacts:id/floating_action_button")
plus_button.click()
drop_downs = driver.find_element(AppiumBy.XPATH,"//android.widget.Spinner[@accessibility id='Mobile Phone']")
drop_downs.click()





