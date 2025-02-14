from selenium.webdriver.common.by import By


class Order:
    search_bar = (By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
    button = (By.XPATH, "//button[@title='Search for Products, Brands and More']")
    pen = (By.XPATH, "//a[@title='CROSS Refill BP Ball Pen Refill']")
    add_cart = (By.XPATH, "//button[@class = 'QqFHMw vslbG+ In9uk2']")
    remove = (By.XPATH,"//div[@class='sBxzFz']")

    def __init__(self, driver):
        self.driver = driver

    def search_text_method(self):
        return self.driver.find_element(*Order.search_bar)

    def search_button_method(self):
        return self.driver.find_element(*Order.button)

    def pen_select_method(self):
        return self.driver.find_element(*Order.pen)

    def add_cart_method(self):
        return self.driver.find_element(*Order.add_cart)

    def remove_cart_method(self):
        return self.driver.find_element(*Order.remove)


