from Email_web.configuration.config import setup
from Email_web.log.log import get_logger
from Email_web.pages.Home_Page import HomePage

class Test_email:

    def Test_sample(self,setup):
        logger = get_logger()

        try:
            logger.info("Test case has started")



        except Exception as msg:
            logger.error(msg)

