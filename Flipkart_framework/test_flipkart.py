import time

from Flipkart_framework.log import get_logger
from Pages.ordering_item import Order


class Test_flipkart:

    def test_order(self, setup):

        logger = get_logger()

        try:
            logger.info("Test has get started")
            Order_obj = Order(self.driver)
            search_var = Order_obj.search_text_method()
            search_var.send_keys("pens")
            time.sleep(5)
            button_search = Order_obj.search_button_method()
            button_search.click()
            time.sleep(5)

            pen_click = Order_obj.pen_select_method()
            pen_click.click()
            time.sleep(5)
            get_handle = self.driver.window_handles
            self.driver.switch_to.window(get_handle[1])
            add_to_cart = Order_obj.add_cart_method()
            add_to_cart.click()
            time.sleep(3)

            remove_cart = Order_obj.remove_cart_method()
            remove_cart.click()
            time.sleep(4)

            logger.info("test case has ended")

        except Exception as msg:
            logger.error(msg)
            raise




