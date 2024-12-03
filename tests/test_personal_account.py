import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Личный кабинет")
@allure.story("Работа с личным кабинетом")
class TestPersonalAccount:
    @allure.title("Тест перехода в личный кабинет")
    def test_go_to_personal_account(self, browser):
        account_page = PersonalAccountPage(browser)

        with allure.step("Открытие главной страницы"):
            account_page.open_url("https://stellarburgers.nomoreparties.site")

        with allure.step("Переход в личный кабинет"):
            account_page.go_to_personal_account()

        with allure.step("Проверка URL страницы логина"):
            account_page.wait_for_url_contains("login")
            assert "login" in account_page.get_current_url()

    @allure.title("Тест перехода в раздел 'История заказов'")
    def test_order_history_navigation(self, browser, test_user):
        login_page = LoginPage(browser)
        account_page = PersonalAccountPage(browser)

        with allure.step("Открытие страницы логина"):
            login_page.open_url("https://stellarburgers.nomoreparties.site/login")

        with allure.step("Авторизация пользователя"):
            login_page.input_email(test_user["user"]["email"])
            login_page.input_password(test_user["user"]["password"])
            login_page.click_login()

        with allure.step("Переход в личный кабинет"):
            account_page.go_to_personal_account()

        with allure.step("Переход в раздел 'История заказов'"):
            account_page.go_to_order_history()
            account_page.wait_for_url_contains("order-history")
            assert "order-history" in account_page.get_current_url()

    @allure.title("Тест выхода из аккаунта")
    def test_logout(self, browser, test_user):
        login_page = LoginPage(browser)
        account_page = PersonalAccountPage(browser)

        with allure.step("Открытие страницы логина"):
            login_page.open_url("https://stellarburgers.nomoreparties.site/login")

        with allure.step("Авторизация пользователя"):
            login_page.input_email(test_user["user"]["email"])
            login_page.input_password(test_user["user"]["password"])
            login_page.click_login()

        with allure.step("Переход в личный кабинет"):
            account_page.go_to_personal_account()

        with allure.step("Выход из аккаунта"):
            account_page.logout()
            account_page.wait_for_url_contains("login")
            assert "login" in account_page.get_current_url()
