import time

from Email.configuration.conftest import setup
from Email.log.log import get_logger
from Email.pages.text_msg import TestMsg
from Email.pages.utils import image_xpath,received_image,image_file


class TestSample:
    def test_sample(self, setup):
        logger = get_logger()

        try:
            logger.info("Test case started")
            TestMsg_obj = TestMsg(self.driver_a,self.driver_b)
            TestMsg_obj.send_mail()
            logger.info("Mail sent successfully")

            TestMsg_obj.attach_image()
            logger.info("Image has been sent")
            logger.info("Checking the mail in the receiver device")
            time.sleep(15)

            TestMsg_obj.verify_email_received()
            logger.info("Email received successfully")

            TestMsg_obj.verify_image_received()

            time.sleep(5)
            logger.info("Email verified successfully")


        except Exception as msg:
            logger.error(msg)





