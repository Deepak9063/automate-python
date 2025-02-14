import allure
from appium.webdriver.common.appiumby import AppiumBy


class Phone:
    def __init__(self,driver):
        self.driver = driver

    dial_pad = (AppiumBy.ID,"com.google.android.dialer:id/dialpad_fab")
    num_seven = (AppiumBy.XPATH,"//android.widget.TextView[@text='7']")
    num_eight = (AppiumBy.XPATH,"//android.widget.TextView[@text='8']")
    num_nine = (AppiumBy.XPATH,"//android.widget.TextView[@text='9']")
    num_two = (AppiumBy.XPATH,"//android.widget.TextView[@text='2']")
    num_one = (AppiumBy.XPATH,"//android.widget.TextView[@text='1']")
    num_zero = (AppiumBy.XPATH,"//android.widget.TextView[@text='0']")
    num_four = (AppiumBy.XPATH,"//android.widget.TextView[@text='4']")
    num_five = (AppiumBy.XPATH,"//android.widget.TextView[@text='5']")
    call_button = (AppiumBy.XPATH,"//android.widget.Button[@content-desc='dial']")
    create_contact = (AppiumBy.XPATH,"//android.widget.TextView[@text='Create new contact']")
    first_name = (AppiumBy.XPATH,"//*[@text='First name']")
    save_contact = (AppiumBy.XPATH,"//android.widget.Button[@text='Save']")


    def dial_key_method(self):
        return self.driver.find_element(*Phone.dial_pad)

    def num_seven_method(self):
        return self.driver.find_element(*Phone.num_seven)

    def num_eight_method(self):
        return self.driver.find_element(*Phone.num_eight)

    def num_nine_method(self):
        return self.driver.find_element(*Phone.num_nine)

    def num_two_method(self):
        return self.driver.find_element(*Phone.num_two)

    def num_one_method(self):
        return self.driver.find_element(*Phone.num_one)

    def num_zero_method(self):
        return self.driver.find_element(*Phone.num_zero)

    def num_four_method(self):
        return self.driver.find_element(*Phone.num_four)

    def num_five_method(self):
        return self.driver.find_element(*Phone.num_five)

    def call_button_method(self):
        return self.driver.find_element(*Phone.call_button)

    def create_contact_method(self):
        return self.driver.find_element(*Phone.create_contact)

    def first_name_method(self):
        return self.driver.find_element(*Phone.first_name)

    def save_contact_method(self):
        return self.driver.find_element(*Phone.save_contact)



























