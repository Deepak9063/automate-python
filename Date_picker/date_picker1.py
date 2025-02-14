import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
date = "03"
month = "September"
year = "2001"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text #this is for month
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text   #this is for year
    if mon==month and yr==year:
        break

    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click() #Next arrow

#Select the dates
dates = driver.find_elements(By.XPATH,"//table[@id='ui-datepicker-div']//table/tbody/tr/td")
for ele in dates:
    if ele.text == date:
        ele.click()
        break

time.sleep(5)

