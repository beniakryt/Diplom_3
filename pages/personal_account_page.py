from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
import allure

class PersonalAccountPage(BasePage):
    @allure.step("Переход в личный кабинет")
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Переход в раздел истории заказов")
    def go_to_order_history(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_SECTION)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step("Переход в личный кабинет")
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Переход в раздел истории заказов")
    def go_to_order_history(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_SECTION)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)