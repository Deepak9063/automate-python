from orange_hrm_automation1.HomePage import HomePage
from orange_hrm_automation1.log import get_logger

class TestOne:
    #@pytest.mark.usefixtures("setup")
    def test_e2e(self,setup):
        #homePage = HomePage(self.driver)
        logger = get_logger()
        try:
            logger.info("Test case started")
            obj1 = HomePage(self.driver)
            username=obj1.username_method()
            username.send_keys("Admin")
            password=obj1.password_method()
            password.send_keys("admin123")

            profile_obj = obj1.click_method()
            profile_obj.PIM_Button().click()
            logger.info("PIM button is clicked")
            logger.info("Test case ends")

        except Exception as msg:
            logger.error(msg)
            raise






        # self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        # time.sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//button[@role='none']").click()

