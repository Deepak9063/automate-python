from selenium.webdriver.common.by import By
from orange_hrm_automation1.profile import Profile


class HomePage:

    def __init__(self,driver):
        self.driver = driver
    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    click_button = (By.XPATH,"//button[@type='submit']")

    def username_method(self):
        return self.driver.find_element(*HomePage.username)

    def password_method(self):
        return self.driver.find_element(*HomePage.password)

    def click_method(self):
        self.driver.find_element(*HomePage.click_button).click()

        profile = Profile(self.driver)
        return profile









