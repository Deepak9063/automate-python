import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.hmh.api",
    "appActivity": ".ApiDemos"
}

url = "http://localhost:4723/wd/hub"
time.sleep(5)
driver = webdriver.Remote(url, desired_capabilities=des_cap)
time.sleep(5)

continue_button = driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/continue_button")
continue_button.click()
time.sleep(2)
ok_button = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='OK']")
ok_button.click()
time.sleep(2)
views = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Views']")
views.click()
gallery = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Gallery']")
gallery.click()
time.sleep(3)
photos = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='1. Photos']")
photos.click()
time.sleep(2)
#scroll to the end horizontally
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
     'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')