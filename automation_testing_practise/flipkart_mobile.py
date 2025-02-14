# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
#
# search_bar = driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']")
# search_bar.send_keys("Mobiles")
# search_enter = driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']//*[name()='svg']")
# search_enter.click()
# time.sleep(3)
#
# mobile_elements = driver.find_elements(By.XPATH,"//div[@class='KzDlHZ']")
# price_elements = driver.find_elements(By.XPATH,"//div[@class='Nx9bqj _4b5DiR']")
#
# print(f"Length of mobile elements: {len(mobile_elements)}")
# print(f"Length of price elements :{len(price_elements)}")
#
# for mobile,price in zip(mobile_elements,price_elements):
#     mobile_name = mobile.text
#     mobile_price = price.text.replace('₹','').replace(',','')
#
#     try:
#






