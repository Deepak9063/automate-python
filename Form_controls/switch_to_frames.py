import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(3)
element = driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']")
element.click()
outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
time.sleep(2)
input_data = driver.find_element(By.XPATH,"//input[@type='text']")
input_data.send_keys("Tiptur")
time.sleep(3)