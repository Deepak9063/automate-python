import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
#driver.get_screenshot_as_base64(os.getcwd()+"\\homepage.png")
time.sleep(4)