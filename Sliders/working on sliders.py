from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/demo-site/sliders/")

min_slider = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/span[1]")

#max_slider = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default ui-state-hover' and @style='left: 60%;']")

print("Location of the slider before moving")
print(min_slider.location)
# print(max_slider.location)

