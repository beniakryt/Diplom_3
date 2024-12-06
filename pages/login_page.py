from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    @allure.step("Переход на страницу восстановления пароля")
    def go_to_password_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step("Ввод email: {email}")
    def input_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке восстановления пароля")
    def click_recover(self):
        self.click_element(LoginPageLocators.RECOVER_BUTTON)

    @allure.step("Переключение видимости пароля")
    def toggle_password_visibility(self):
        self.click_element(LoginPageLocators.TOGGLE_PASSWORD_BUTTON)

    @allure.step("Проверка активности поля")
    def is_field_active(self):
        field_div = self.find_element(LoginPageLocators.TOGGLE_PASSWORD_BUTTON_ACTIVE)
        field_class = field_div.get_attribute("class")
        return "input_status_active" in field_class

    @allure.step("Ввод пароля: {password}")
    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке входа")
    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        self.open_url("https://stellarburgers.nomoreparties.site/login")

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        self.open_url("https://stellarburgers.nomoreparties.site/forgot-password")