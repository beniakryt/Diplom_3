from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    @allure.step("Клик по элементу ленты заказов")
    def click_order_feed_item(self):
        self.click_element(OrderPageLocators.ORDER_FEED_ITEM)

    @allure.step("Проверка видимости всплывающего окна заказа")
    def is_order_popup_visible(self):
        return self.is_element_visible(OrderPageLocators.ORDER_DETAILS_POPUP)

    @allure.step("Закрытие всплывающего окна заказа")
    def close_order_popup(self):
        self.click_element(OrderPageLocators.ORDER_DETAILS_CLOSE_BUTTON)

    @allure.step("Получение количества завершённых заказов за всё время")
    def get_completed_count_all_time(self):
        element = self.find_element(OrderPageLocators.ORDER_COMPLETED_ALL_TIME)
        return int(element.text)

    @allure.step("Получение количества завершённых заказов за сегодня")
    def get_completed_count_today(self):
        element = self.find_element(OrderPageLocators.ORDER_COMPLETED_TODAY)
        return int(element.text)

    @allure.step("Получение списка всех заказов в процессе выполнения")
    def get_all_orders_in_progress(self):
        elements = self.find_elements(OrderPageLocators.ORDER_LIST_IN_PROGRESS)
        return [element.text for element in elements]

    @allure.step("Получение списка всех заказов в ленте")
    def get_all_orders_in_feed(self):
        elements = self.find_elements(OrderPageLocators.ORDER_LIST_IN_FEED)
        return [element.text for element in elements if element.text.startswith("#")]

    @allure.step("Открытие страницы ленты заказов")
    def open_feed_page(self):
        self.open_url("https://stellarburgers.nomoreparties.site/feed")