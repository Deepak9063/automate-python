import pytest
from appium import webdriver
from Appium_Framework1.configuration.config import url,cap

@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Remote(url,cap)
    driver.implicitly_wait(5)
    request.cls.driver=driver
    yield
    driver.quit()



