from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://doubleclicktest.com/")

double_click_button = driver.find_element(By.XPATH,"")


