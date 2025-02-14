from selenium import webdriver
from selenium.webdriver.common.by import By

#For disabling the popups we use this
ops = webdriver.ChromeOptions()
ops.add_argument("--Disable-notifications")

driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/")



