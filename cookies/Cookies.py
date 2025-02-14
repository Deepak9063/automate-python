import cookies
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies = driver.get_cookies()
print("Initial length od cookie",len(cookies))

for c in cookies:
    print(c.get('name'))

#Adding the cookies
driver.add_cookie({"name":"Mycookie","value":"1234567"})
updated_cookie = driver.get_cookies()
print(len("Length of the cookie after updating",updated_cookie))

driver.delete_all_cookies()
deleted_cookie = driver.get_cookies()
print("Length of the cookie after deleting",len(deleted_cookie))