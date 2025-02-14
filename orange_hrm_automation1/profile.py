from selenium.webdriver.common.by import By


class Profile:
    def __init__(self,driver):
        self.driver = driver
    PIM = (By.XPATH,"//a[@href='/web/index.php/dashboard/index']")




    def PIM_Button(self):
        return self.driver.find_element(*Profile.PIM)







