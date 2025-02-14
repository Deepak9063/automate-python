import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def take_screenshot(self, driver, filename):

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = rf"C:\Users\deepa\PycharmProjects\pythonProjectAppium\Appium_Framework1\Screenshots\{filename}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
    def get_element(self,driver,locator_type,locator_value):
        try:
            wait=WebDriverWait(driver,30)
            if locator_type=="id":
                element=wait.until(EC.presence_of_element_located((By.ID,locator_value)))
                return element
            elif locator_type=="xpath":
                element=wait.until(EC.presence_of_element_located((By.XPATH,locator_value)))
                return element
            elif locator_type=="css selector":
                element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,locator_value)))
                return element
            elif locator_type=="link text":
                element=wait.until(EC.presence_of_element_located((By.LINK_TEXT,locator_value)))
                return element

            else:
                print("element not matching.Taking ScreenShot")
                self.take_screenshot(driver, "get_element_error")
                return None

        except Exception as e:
            self.take_screenshot(driver,"get_element_exception")

    def click_element(self,driver,locator_type,locator_value):
        try:
            element=self.get_element(driver,locator_type,locator_value)
            element.click()
        except Exception as msg:
            self.take_screenshot(driver, "click_element_error")
            print(msg)


    def send_text(self,driver,locator_type,locator_value,text):
        try:
            element=self.get_element(driver,locator_type,locator_value)
            element.send_keys(text)
        except Exception as msg:
            self.take_screenshot(driver, "send_text_error")
            print(msg)

    def get_text(self,driver,locator_type,locator_value):
        try:
            element=self.get_element(driver,locator_type,locator_value)
            element.text()

        except Exception as msg:
            self.take_screenshot(driver, "get_text_error")
            print(msg)

    def isDisplayed(self,driver,locator_type,locator_value):
        try:
            element=self.get_element(driver,locator_type,locator_value)
            element.is_displayed()
        except Exception as msg:
            self.take_screenshot(driver, "isDisplayed_error")
            print(msg)

    def clear(self,driver,locator_type,locator_value):
        try:
            element=self.get_element(driver,locator_type,locator_value)
            element.clear()
        except Exception as msg:
            self.take_screenshot(driver, "clear_error")
            print(msg)

