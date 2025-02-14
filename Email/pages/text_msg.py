import logging
import os

from Email.BaseClass.BaseClass import BaseClass
from . import utils
from Email.log.log import get_logger


BaseClass_obj = BaseClass()
header_text = "Testing"


class TestMsg:
    def __init__(self, driver_a, driver_b):
        self.driver_a = driver_a
        self.driver_b = driver_b

    def send_mail(self):

        BaseClass_obj.click_element(self.driver_a, "xpath", utils.compose_button)
        BaseClass_obj.send_text(self.driver_a, "xpath", utils.add_to_mail_address, "pavan.b@lirisoft.com")
        BaseClass_obj.click_element(self.driver_a, "xpath", utils.click_on_email)
        BaseClass_obj.send_text(self.driver_a, "xpath", utils.header, header_text)


    def attach_image(self):
        BaseClass_obj.click_element(self.driver_a,"xpath",utils.link_button)
        BaseClass_obj.click_element(self.driver_a,"xpath",utils.attach_file_button)
        BaseClass_obj.click_element(self.driver_a,"xpath",utils.image_file)
        BaseClass_obj.click_element(self.driver_a, "id", utils.send_button)

    def verify_email_received(self):
        received_header = BaseClass_obj.get_text(self.driver_b, "xpath", utils.testing_mail)
        print(f"Received Header,{received_header}")
        if received_header is not None:
            if received_header == header_text:
                print("Email received successfully with the same header.")
            else:
                print(f"Email received successfully with a different header: {received_header}")
        else:
            print("Failed to retrieve the received email header.")



    def verify_image_received(self):
        BaseClass_obj.click_element(self.driver_b, "xpath", utils.received_email)
        #BaseClass_obj.click_element(self.driver_b,"xpath",utils.received_image)

        #for openeing the image in sender side
        BaseClass_obj.click_element(self.driver_a,"xpath",utils.navigation_bar)
        BaseClass_obj.click_element(self.driver_a,"xpath",utils.sent_button)
        BaseClass_obj.click_element(self.driver_a,"xpath",utils.sent_mail_click)
        #BaseClass_obj.click_element(self.driver_a,"xpath",utils.image_click)

        received_image_element = BaseClass_obj.get_text(self.driver_b, "xpath", utils.received_image)
        attached_image_element = BaseClass_obj.get_text(self.driver_a, "xpath", utils.image_file)

        #First it will fetch the receiver side image text
        r = BaseClass_obj.text_we_got
        print("Receiver_side",r)

        #Second it will fetch the sender side image text
        s = BaseClass_obj.text_we_got
        print("Sender_side",s)

        if received_image_element and attached_image_element is not None:
            if received_image_element == attached_image_element:
                print("Both the images are the same.")
            else:
                print("Both the images are different.")
        else:
            print("One or both image elements were not found.")




























































































































































