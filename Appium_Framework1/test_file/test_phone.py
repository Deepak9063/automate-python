import time

from Appium_Framework1.configuration.conftest import setup
from Appium_Framework1.log.log import get_logger
from Appium_Framework1.pages.contact_save import Homepage
class TestSample:

    def test_sample(self, setup):
        logger = get_logger()
        try:
            logger.info("test case starts")
            Homepage_obj = Homepage(self.driver)
            Homepage_obj.create_contact()
            logger.info("Contact has been saved")
            Homepage_obj.send_text()
            logger.info("Message has been sent")


        except Exception as msg:
            logger.error(msg)


