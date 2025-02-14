import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")

developer_button = driver.find_element(By.XPATH,"//button[@id='developers-dd-toggle']")
support = driver.find_element(By.XPATH,"//a[@title='Support']//span[@class='item-text'][normalize-space()='Support']")

#mouse hover
act = ActionChains(driver)
act.move_to_element(developer_button).move_to_element(support).click().perform()
time.sleep(3)

search = driver.find_element(By.XPATH,"//input[@id='main-content']")
search.send_keys("local testing")
time.sleep(3)
# To click on enter
driver.find_element(By.XPATH,"//button[@id='search-support-search-submit']").click()
time.sleep(4)