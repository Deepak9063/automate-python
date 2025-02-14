import pytest
from appium import webdriver
from Email.configuration.config import cap_device_A,cap_device_B,url


@pytest.fixture(scope="class")
def setup(request):
    #Desired capabilities for device1
    driver_a = webdriver.Remote(url,cap_device_A)
    driver_a.implicitly_wait(5)
    request.cls.driver_a = driver_a

    #Desired capabalities for device2
    driver_b = webdriver.Remote(url,cap_device_B)
    driver_b.implicitly_wait(5)
    request.cls.driver_b = driver_b

    yield
    driver_a.quit()
    driver_b.quit()