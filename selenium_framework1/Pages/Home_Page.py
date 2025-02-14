from selenium_framework1.Base_class.BaseClass import BaseClass
from selenium_framework1.Pages.utils import username,password,login_button,admin_button,Username

baseclass_obj = BaseClass()
class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def login_method(self):
        baseclass_obj.send_text(self.driver,"xpath",username,"Admin")
        baseclass_obj.send_text(self.driver,"xpath",password,"admin123")
        baseclass_obj.click_element(self.driver,"xpath",login_button)
        baseclass_obj.send_text(self.driver,"xpath",Username,"Deepak")

    def admin_page_method(self):
        baseclass_obj.click_element(self.driver,"xpath",admin_button)








