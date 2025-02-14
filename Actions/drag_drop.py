import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.mobeta.android.demodslv",
    "appActivity": ".Launcher"
}

url = "http://localhost:4723/wd/hub"

driver = webdriver.Remote(url,desired_capabilities=des_cap)
continue_button = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Continue']")
continue_button.click()
time.sleep(2)
ok_button = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='OK']")
ok_button.click()
basic_usage = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Basic usage playground']")
basic_usage.click()









