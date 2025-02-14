import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                            ElementNotVisibleException,
                                                            ElementNotSelectableException,
                                                            Exception]
                       )
searchLink = mywait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='APjFqb']")))

#searchLink = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
searchLink.send_keys("Tiptur")
searchLink.submit()



