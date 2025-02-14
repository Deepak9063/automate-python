import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

des_cap = {
    "platformName": "Android",
    "deviceName": "ZD2224LD3H",
    "automationName": "uiAutomator2",
    "appPackage": "com.flipkart.android",
    "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity"
}

appium_server_url = "http://localhost:4723/wd/hub"

driver = webdriver.Remote(appium_server_url,des_cap)
wait = WebDriverWait(driver,10)
ele = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.flipkart.android:id/custom_back_icon")))
ele.click()

search = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")))
search.sendKeys("Bags")
# element_cancel = driver.find_element(AppiumBy.ID,"com.flipkart.android:id/custom_back_icon")
# time.sleep(5)
# element_cancel.click()




element_continue = driver.find_element(AppiumBy.XPATH,"com.flipkart.android:id/select_btn")
# element_continue.click()
