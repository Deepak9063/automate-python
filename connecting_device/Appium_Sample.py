from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    "platformName" : "Android",
    "deviceName" : "ZD2224LD3H",
    "automationName" : "uiAutomator2",
    "appPackage" : "com.google.android.calculator",
    "appActivity" : "com.android.calculator2.Calculator"


}
appium_server_url= "http://localhost:4723/wd/hub"

driver = webdriver.Remote(appium_server_url,desired_cap)

element7 = driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/digit_7")
element7.click()
element_multiply = driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/op_mul")
element_multiply.click()
element2 = driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/digit_2")
element2.click()

attribute_value = element2.get_attribute("class")
print(attribute_value)  #here this gives me the attribute value

#driver.close()

#element5 = driver.find_elements(AppiumBy.ID,"")

