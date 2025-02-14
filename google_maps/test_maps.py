from google_maps.log import get_logger
from google_maps.Pages.Home_page import HomePage
class TestOne:
    def test_maps(self,setup):
        logger = get_logger()

        try:
            logger.info("Test case has started")
            Home = HomePage(self.driver)
            search_text = Home.search_method()
            search_text.send_keys("Tiptur")

            click_restaurant = Home.restaurant_button_method()
            click_restaurant.click()

            logger.info("Test case ends")

        except Exception as msg:
            logger.error(msg)
            raise













