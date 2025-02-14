from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def headless_chrome():
    options = Options()
    options.add_argument('--headless')  # Enable headless mode
    driver = webdriver.Chrome(service=Service(), options=options)
    return driver

driver = headless_chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)  # Check that the page has loaded
driver.quit()

