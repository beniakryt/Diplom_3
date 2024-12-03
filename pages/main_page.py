from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step("Клик по кнопке конструктора")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке ленты")
    def click_feed(self):
        self.click_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        ingredient = self.find_element(MainPageLocators.FIRST_INGREDIENT)
        order_area = self.find_element(MainPageLocators.ORDER_AREA)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, order_area).perform()

    @allure.step("Получение счётчика ингредиентов")
    def get_ingredient_counter(self):
        counter = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    @allure.step("Отправка заказа")
    def submit_order(self):
        self.click_element(MainPageLocators.SUBMIT_ORDER_BUTTON)

    @allure.step("Проверка успешности заказа")
    def is_order_successful(self):
        return self.is_element_visible(MainPageLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step("Проверка, что пользователь находится на главной странице")
    def is_on_main_page(self):
        return "https://stellarburgers.nomoreparties.site" in self.get_current_url()

    @allure.step("Клик по первому ингредиенту")
    def click_ingredient(self):
        self.wait_for_element_clickable(MainPageLocators.FIRST_INGREDIENT).click()

    @allure.step("Проверка видимости всплывающего окна ингредиента")
    def is_popup_visible(self):
        return self.wait_for_element_visible(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step("Закрытие всплывающего окна ингредиента")
    def close_popup(self):
        self.wait_for_element_clickable(MainPageLocators.CLOSE_POPUP_BUTTON).click()
        self.wait_for_element_invisible(MainPageLocators.INGREDIENT_DETAILS_POPUP)
