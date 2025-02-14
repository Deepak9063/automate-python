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
driver = webdriver.Remote(url,desired_capabilities=des_cap)
continue_button=driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Continue']")
continue_button.click()
time.sleep(2)
ok_button = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='OK']")
ok_button.click()
time.sleep(2)
app = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='App']")
app.click()
time.sleep(2)
alert_box = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Alert Dialogs']")
alert_box.click()
ele1 = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='OK Cancel dialog with a message']")
ele1.click()
time.sleep(1)
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()












