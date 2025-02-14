import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver=driver
    yield
    driver.quit()
