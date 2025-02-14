import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def driver_setup():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    return driver
class Myntra:
    def __init__(self,driver):
        self.driver = driver

    def search_bar(self):
        self.driver.find_element(By.XPATH,"//input[@id='search']").send_keys("Mens clothing")
        self.driver.find_element(By.XPATH,"//div[@class='yt-spec-touch-feedback-shape__stroke']").click()
        my_alert=driver.switch_to.alert
        my_alert.accept()
        #self.driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']").click()
        time.sleep(4)

driver = driver_setup()
test_obj = Myntra(driver)
test_obj.search_bar()



