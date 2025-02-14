import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")
name = driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys("Deepak T M")

search = driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
search.send_keys("selenium")
time.sleep(5)
click_search = driver.find_element(By.XPATH,"//input[@type='submit']")
click_search.click()
time.sleep(5)
#To find all the elements we use this xpath and we find the common xpath b/w the elemets
different_search = driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']")
print(len(different_search))
for ele in different_search:
    print(ele.text)

if len(different_search)>1:
    different_search[2].click()
time.sleep(3)


check_box = driver.find_element(By.XPATH,"//input[@id='male']")
check_box.click()
time.sleep(5)

