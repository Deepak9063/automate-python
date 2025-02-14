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
app_button = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='App']")
app_button.click()
time.sleep(2)
activity_button = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Activity']")
activity_button.click()

#It scrolls until it finds the element
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Wallpaper"))').click()

#This is to scrolldown till the end..
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(5)')

#scroll_horizontal
# # Scroll to the end horizontally
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')
#
# # Scroll to the beginning horizontally
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(5)')
#



# print(device_size)
# screenWidth = device_size['width']
# screenHeight = device_size['height']
# print(screenWidth)
# print(screenHeight)
#
# startX = screenWidth/2
# endY = screenHeight/2















