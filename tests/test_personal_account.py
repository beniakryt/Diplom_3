from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from locators.personal_account_locators import PersonalAccountLocators


@allure.feature("Личный кабинет")
def test_go_to_personal_account(browser):
    browser.get("https://stellarburgers.nomoreparties.site")
    account_page = PersonalAccountPage(browser)

    with allure.step("Переход в личный кабинет"):
        account_page.go_to_personal_account()

        WebDriverWait(browser, 10).until(
            EC.url_contains("login")
        )
        assert "login" in browser.current_url


@allure.feature("Личный кабинет")
def test_order_history_navigation(browser, test_user):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(browser)

    with allure.step("Авторизация пользователя"):
        login_page.input_email(test_user["user"]["email"])
        login_page.input_password(test_user["user"]["password"])
        login_page.click_login()

    account_page = PersonalAccountPage(browser)
    with allure.step("Переход в личный кабинет"):
        account_page.go_to_personal_account()

    with allure.step("Переход в раздел 'История заказов'"):
        account_page.go_to_order_history()

        WebDriverWait(browser, 10).until(
            EC.url_contains("order-history")
        )

        assert "order-history" in browser.current_url


@allure.feature("Личный кабинет")
def test_logout(browser, test_user):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(browser)

    with allure.step("Авторизация пользователя"):
        login_page.input_email(test_user["user"]["email"])
        login_page.input_password(test_user["user"]["password"])
        login_page.click_login()

    account_page = PersonalAccountPage(browser)
    with allure.step("Переход в личный кабинет"):
        account_page.go_to_personal_account()

    account_page = PersonalAccountPage(browser)
    with allure.step("Выход из аккаунта"):
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        account_page.logout()

        WebDriverWait(browser, 10).until(
            EC.url_contains("login")
        )

        assert "login" in browser.current_url
