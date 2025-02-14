import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
element = driver.find_element(By.XPATH,"//input[@name='username']")
element.send_keys("Admin")
time.sleep(3)
element1 = driver.find_element(By.CSS_SELECTOR,"input[type=password]")
element1.send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(5)
print(driver.title)
act_title = driver.title
exp_title = "OrangeHRM"

if act_title==exp_title:
    print("Login successful")
else:
    print("Login not successful")


























 

