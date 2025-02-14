from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tus.io/demo")
driver.find_element(By.XPATH,"//input[@id='P0-0']").send_keys("C:\Users\deepa\Downloads\file-sample_100kB (1).doc")


