from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
def test_go_to_password_recovery(browser):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(browser)

    with allure.step("Переход на страницу восстановления пароля"):
        login_page.go_to_password_recovery()

        WebDriverWait(browser, 10).until(
            EC.url_contains("forgot-password")
        )
        assert "forgot-password" in browser.current_url



@allure.feature("Восстановление пароля")
def test_password_recovery_submit(browser):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(browser)

    with allure.step("Ввод email и клик по кнопке восстановления"):
        login_page.go_to_password_recovery()
        login_page.input_email("yurii142323223@yandex.ru")
        login_page.click_recover()

        expected_url = "https://stellarburgers.nomoreparties.site/reset-password"

        # Ожидание перехода на URL восстановления
        WebDriverWait(browser, 10).until(
            EC.url_to_be(expected_url)
        )
        assert browser.current_url == expected_url


@allure.feature("Восстановление пароля")
def test_toggle_password_visibility(browser):
    login_page = LoginPage(browser)
    browser.get("https://stellarburgers.nomoreparties.site/forgot-password")

    with allure.step("Клик по кнопке 'Восстановить пароль'"):
        login_page.click_recover()

        # Ожидание, что URL изменится на reset-password
        WebDriverWait(browser, 10).until(
            EC.url_contains("reset-password")
        )

    with allure.step("Клик по кнопке 'Показать/Скрыть пароль'"):
        login_page.toggle_password_visibility()

        # Ожидание, что поле станет активным
        WebDriverWait(browser, 10).until(
            lambda driver: login_page.is_field_active()
        )

        assert login_page.is_field_active()
