from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_feed_item(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_FEED_ITEM)
        ).click()

    def is_order_popup_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_DETAILS_POPUP)
        ).is_displayed()

    def close_order_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_DETAILS_CLOSE_BUTTON)
        ).click()

    def get_completed_count_all_time(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED_ALL_TIME)
        )
        return int(element.text)

    def get_completed_count_today(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED_TODAY)
        )
        return int(element.text)

    def get_all_orders_in_progress(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(OrderPageLocators.ORDER_LIST_IN_PROGRESS)
        )
        elements = self.driver.find_elements(*OrderPageLocators.ORDER_LIST_IN_PROGRESS)
        return [element.text for element in elements]

    def get_all_orders_in_feed(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(OrderPageLocators.ORDER_LIST_IN_FEED)
        )
        elements = self.driver.find_elements(*OrderPageLocators.ORDER_LIST_IN_FEED)
        return [element.text for element in elements if element.text.startswith("#")]
