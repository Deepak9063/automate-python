import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.implicitly_wait(10)#It waits only when synchronization problem is there
element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(element.is_displayed())
print(element.is_enabled())
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(rd_male.is_selected())

rd_male.click()
rd_female.click()

print("It is selecting the male radio button",rd_male.is_selected())
print("It is selecting the female radio button",rd_female.is_selected())
