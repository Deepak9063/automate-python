import time

import allure
from allure_commons.types import AttachmentType
from Emulator5554_Automation.conftest import setup
from Emulator5554_Automation.log import get_logger
from Emulator5554_Automation.phone import Phone


class Test_app:


    def test_mobile_app(self,setup):
        logger = get_logger()

        try:
            logger.info("Testing has started")
            phone_obj = Phone(self.driver)
            dial = phone_obj.dial_key_method()
            dial.click()

            num_seven = phone_obj.num_seven_method()
            num_seven.click()
            num_eight = phone_obj.num_eight_method()
            num_eight.click()
            num_nine = phone_obj.num_nine_method()
            num_nine.click()
            num_two = phone_obj.num_two_method()
            num_two.click()
            num_one = phone_obj.num_one_method()
            num_one.click()
            num_one.click()
            num_nine.click()
            num_zero = phone_obj.num_zero_method()
            num_zero.click()
            num_four = phone_obj.num_four_method()
            num_four.click()
            num_five = phone_obj.num_five_method()
            num_five.click()
            call_button = phone_obj.call_button_method()
            call_button.click()
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
            logger.info("It has completed pressing all the numbers")

            create_contact = phone_obj.create_contact_method()
            create_contact.click()
            time.sleep(5)
            first_name = phone_obj.first_name_method()
            first_name.click()
            first_name.send_keys("Deepak")
            time.sleep(2)
            save_contact = phone_obj.save_contact_method()
            save_contact.click()


            logger.info("Test has ended")




        except Exception as msg:
            logger.error(msg)
            raise
