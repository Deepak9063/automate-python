from Appium_Framework1.BaseClass.BaseClass import BaseClass
from . import utils

baseclass_obj = BaseClass()

class Homepage:

    def __init__(self, driver):
        self.driver = driver
    def create_contact(self):
        baseclass_obj.click_element(self.driver,"xpath",utils.contacts_button)
        baseclass_obj.click_element(self.driver,"xpath",utils.create_new_contact)
        baseclass_obj.send_text(self.driver,"xpath",utils.first_name,"Chandan")
        baseclass_obj.send_text(self.driver,"xpath",utils.last_name,"TM")
        baseclass_obj.send_text(self.driver,"xpath",utils.phone_num,"9535079130")
        baseclass_obj.click_element(self.driver,"xpath",utils.save_button)

    def send_text(self):
        baseclass_obj.click_element(self.driver,"xpath",utils.chandan_contact)
        baseclass_obj.click_element(self.driver,"xpath",utils.text_button)
        baseclass_obj.send_text(self.driver,"xpath",utils.send_message,"Hii chandan how are you")
        baseclass_obj.click_element(self.driver,"xpath",utils.sms_send_button)

    def delete_text(self):
        baseclass_obj.right_click(self.driver,"xpath",utils.text_message)













