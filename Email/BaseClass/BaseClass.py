import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    text_we_got = None
    def take_screenshot(self, driver, filename):

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = rf"C:\Users\deepa\PycharmProjects\pythonProjectAppium\Appium_Framework1\Screenshots\{filename}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    def get_element(self, driver, locator_type, locator_value):
        try:
            wait = WebDriverWait(driver, 30)
            if locator_type == "id":
                element = wait.until(EC.presence_of_element_located((AppiumBy.ID, locator_value)))
                return element
            elif locator_type == "xpath":
                element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator_value)))
                return element
            elif locator_type == "css selector":
                element = wait.until(EC.presence_of_element_located((AppiumBy.CSS_SELECTOR, locator_value)))
                return element
            elif locator_type == "link text":
                element = wait.until(EC.presence_of_element_located((AppiumBy.LINK_TEXT, locator_value)))
                return element
            else:
                print("element not matching. Taking ScreenShot")
                self.take_screenshot(driver, "get_element_error")
                return None

        except Exception as e:
            self.take_screenshot(driver, "get_element_exception")

    def click_element(self, driver, locator_type, locator_value):
        try:
            element = self.get_element(driver, locator_type, locator_value)
            element.click()
        except Exception as msg:
            self.take_screenshot(driver, "click_element_error")
            print(msg)

    def right_click(self, driver, locator_type, locator_value):
        element = self.get_element(driver, locator_type, locator_value)
        try:
            actions = TouchAction(driver)
            actions.long_press(element).release().perform()
        except Exception as msg:
            self.take_screenshot(driver, "right_click_error")
            print(msg)

    def send_text(self, driver, locator_type, locator_value, text):
        try:
            element = self.get_element(driver, locator_type, locator_value)
            element.send_keys(text)
        except Exception as msg:
            self.take_screenshot(driver, "send_text_error")
            print(msg)

    def get_text(self, driver, locator_type, locator_value):

        try:
            element = self.get_element(driver, locator_type, locator_value)
            self.text_we_got = element.text
        except Exception as msg:
            self.take_screenshot(driver, "get_text_error")
            print(msg)
        return self.text_we_got

    def isDisplayed(self, driver, locator_type, locator_value):
        try:
            element = self.get_element(driver, locator_type, locator_value)
            element.is_displayed()
        except Exception as msg:
            self.take_screenshot(driver, "isDisplayed_error")
            print(msg)

    def clear(self, driver, locator_type, locator_value):
        try:
            element = self.get_element(driver, locator_type, locator_value)
            element.clear()
        except Exception as msg:
            self.take_screenshot(driver, "clear_error")
            print(msg)

    def get_attribute(self, driver, locator_type, locator_value, attribute):
        try:
            element = self.get_element(driver, locator_type, locator_value)
            if element is not None:
                return element.get_attribute(attribute)
            else:
                print(f"Element not found for {locator_value}")
                return None
        except Exception as msg:
            self.take_screenshot(driver, "get_attribute_error")
            print(msg)


