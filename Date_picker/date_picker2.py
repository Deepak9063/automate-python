import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//input[@id='dob']").click()

select_month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
select_month.select_by_visible_text("Oct")
time.sleep(3)
select_year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
select_year.select_by_visible_text("2001")
time.sleep(2)

alldate = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for date in alldate:
    if date.text=="3":
        date.click()
        break

time.sleep(5)










