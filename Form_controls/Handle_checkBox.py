from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")
checkBox = driver.find_element(By.XPATH,"//input[@id='checkbox1']")
checkBox.click()

