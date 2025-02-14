import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")

img = driver.find_element(By.XPATH,"//div[@id='box4']")
target = driver.find_element(By.XPATH,"//div[@id='box106']")

washington = driver.find_element(By.XPATH,"//div[@id='box3']")
united_states = driver.find_element(By.XPATH,"//div[@id='box103']")
act = ActionChains(driver)
act.drag_and_drop(img,target).perform()
#time.sleep(5)
act.drag_and_drop(washington,united_states)
time.sleep(5)
