from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search = (By.XPATH,"//input[@id='searchboxinput']")
    restaurant_button = (By.XPATH,"//button[@aria-label='Restaurants']")
    def search_method(self):
        return self.driver.find_element(*HomePage.search)

    def restaurant_button_method(self):
        return self.driver.find_element(*HomePage.restaurant_button)







