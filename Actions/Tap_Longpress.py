import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

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

element = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name']")

actions = TouchAction(driver)
actions.tap(element).perform().release()



