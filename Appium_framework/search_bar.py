from appium.webdriver.common.appiumby import AppiumBy
class Search:

    def __init__(self,driver):
        self.driver = driver

    search_bar = (AppiumBy.ID,"com.google.android.googlequicksearchbox:id/googleapp_search_box")
    search_button = (AppiumBy.XPATH,"android.widget.ImageView")


    def search_text_method(self):
        return self.driver.find_element(*Search.search_bar)

    def search_button_method(self):
        return self.driver.find_element(*Search.search_button)












