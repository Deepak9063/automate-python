import time
from appium.webdriver.common.touch_action import TouchAction

from Appium_framework.log import get_logger
from Appium_framework.search_bar import Search
class Test_app:
    def test_google_app(self,setup):
        logger = get_logger()

        try:
            logger.info("Testing has started")

            search_obj = Search(self.driver)
            search_var = search_obj.search_text_method()
            search_var.send_keys("Tiptur")
            time.sleep(3)
            search_button = search_obj.search_button_method()
            search_button.click()





        except Exception as msg:
            logger.error(msg)



