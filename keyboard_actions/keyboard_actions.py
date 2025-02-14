import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()
input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Hi this is Deepak how are you")
time.sleep(5)
act = ActionChains(driver)
#This is to press ctrl+a
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#This is to press the ctrl+c
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#This is to switch between the tab
act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)








