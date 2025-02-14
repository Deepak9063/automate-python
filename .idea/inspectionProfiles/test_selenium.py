from selenium import webdriver

#browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser = webdriver.Edge()
browser.get("https://selenium.dev/")
browser.maximize_window()
print(browser.title)