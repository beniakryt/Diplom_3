import allure
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
@allure.story("Функционал восстановления пароля")
class TestPasswordRecovery:
    @allure.title("Тест перехода на страницу восстановления пароля")
    def test_go_to_password_recovery(self, browser):
        login_page = LoginPage(browser)

        with allure.step("Открытие страницы логина"):
            login_page.open_login_page()

        with allure.step("Переход на страницу восстановления пароля"):
            login_page.go_to_password_recovery()

        with allure.step("Проверка URL страницы восстановления пароля"):
            login_page.wait_for_url_contains("forgot-password")
            assert "forgot-password" in login_page.get_current_url()

    @allure.title("Тест отправки формы восстановления пароля")
    def test_password_recovery_submit(self, browser):
        login_page = LoginPage(browser)

        with allure.step("Открытие страницы логина"):
            login_page.open_login_page()

        with allure.step("Ввод email и отправка формы восстановления"):
            login_page.go_to_password_recovery()
            login_page.input_email("yurii142323223@yandex.ru")
            login_page.click_recover()

        with allure.step("Ожидание перехода на страницу сброса пароля"):
            login_page.wait_for_url_contains("reset-password")
            assert "reset-password" in login_page.get_current_url()

    @allure.title("Тест переключения видимости пароля")
    def test_toggle_password_visibility(self, browser):
        login_page = LoginPage(browser)

        with allure.step("Открытие страницы восстановления пароля"):
            login_page.open_forgot_password_page()

        with allure.step("Клик по кнопке 'Восстановить пароль'"):
            login_page.click_recover()
            login_page.wait_for_url_contains("reset-password")

        with allure.step("Переключение видимости пароля"):
            login_page.toggle_password_visibility()
            assert login_page.is_field_active()
