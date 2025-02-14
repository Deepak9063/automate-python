import time


from selenium import webdriver as selenium_webdriver, webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def driver_browser():
    # options = Options()
    # options.headless = False  # Running Firefox in headless mode

   # driver = selenium_webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get("https://gmail.com")
    email = driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']")
    email.send_keys("deepakshetty1253@gmail.com")

    next_button = driver.find_element(By.XPATH,
                                      "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
    next_button.click()
    time.sleep(300)


selenium = driver_browser()


# def driver_device():
#     desired_capabilities_device1 = {
#         "platformName": "Android",
#         "platformVersion": "10",
#         "deviceName": "Galaxy S9",
#         "udid": "5839545034573398",
#         "appPackage": "com.verizon.messaging.vzmsgs",
#         "appActivity": "com.verizon.messaging.vzmsgs.ux.conversation.activity.ConversationListActivity",
#         "noReset": True,
#         "Reset": False,
#         "newCommandTimeout": 1200,
#         "automationName": "UiAutomator2"
#     }
#
#     print(desired_capabilities_device1["deviceName"])
#     print("Sender Device")
#     receiver_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities_device1)
#     return receiver_driver
#
#

# Appium = driver_device()
