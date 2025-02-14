from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']").send_keys("Pens")
driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='GO TO CART'][1]")
