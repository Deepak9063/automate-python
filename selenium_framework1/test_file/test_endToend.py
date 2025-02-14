import time

from selenium_framework1.configuration.conftest import setup
from selenium_framework1.log.log import get_logger
from selenium_framework1.Pages.Home_Page import HomePage
class Test_sample:

    def test_sample(self,setup):
        logger = get_logger()

        try:
            logger.info("Test case starts")
            Homepage_obj = HomePage(self.driver)
            logger.info("Login method test case starts here")
            Homepage_obj.login_method()
            logger.info("Login method test case ends here")
            logger.info("admin_method test case starts here")
            Homepage_obj.admin_page_method()
            time.sleep(5)
            logger.info("admin_method test case ends here")
            logger.info("Test case ends here")

        except Exception as msg:
            logger.error(msg)



