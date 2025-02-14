import pytest
from appium import webdriver
from Appium_framework.config import desired_cap

@pytest.fixture(scope="class")
def setup(request):
    appium_server_url = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(appium_server_url,desired_cap)
    request.cls.driver = driver
    yield
    driver.close()




