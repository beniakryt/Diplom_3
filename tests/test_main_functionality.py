import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage



@allure.feature("Основной функционал")
@allure.story("Переходы")
class TestNavigation:
    @allure.title("Тест перехода к конструктору")
    def test_constructor_navigation(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открытие страницы логина"):
            main_page.open_url("https://stellarburgers.nomoreparties.site/login")

        with allure.step("Переход к конструктору"):
            main_page.click_constructor()
            assert main_page.is_on_main_page()

    @allure.title("Тест перехода к ленте заказов")
    def test_feed_navigation(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открытие главной страницы"):
            main_page.open_url("https://stellarburgers.nomoreparties.site")

        with allure.step("Клик по ленте заказов"):
            main_page.click_feed()

        with allure.step("Проверка URL"):
            main_page.wait_for_url_contains("feed")


@allure.feature("Основной функционал")
@allure.story("Работа с ингредиентами")
class TestIngredients:
    @allure.title("Тест открытия деталей ингредиента")
    def test_ingredient_details_popup_open(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открытие главной страницы"):
            main_page.open_url("https://stellarburgers.nomoreparties.site")

        with allure.step("Клик по ингредиенту"):
            main_page.click_ingredient()

        with allure.step("Проверка видимости всплывающего окна"):
            assert main_page.is_popup_visible()

    @allure.title("Тест закрытия всплывающего окна ингредиента")
    def test_ingredient_details_popup_close(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открытие главной страницы"):
            main_page.open_url("https://stellarburgers.nomoreparties.site")

        with allure.step("Клик по ингредиенту"):
            main_page.click_ingredient()

        with allure.step("Закрытие всплывающего окна"):
            main_page.close_popup()

    @allure.title("Тест увеличения счётчика ингредиентов")
    def test_ingredient_counter_increase(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открытие главной страницы"):
            main_page.open_url("https://stellarburgers.nomoreparties.site")

        with allure.step("Получение начального значения счётчика"):
            initial_count = main_page.get_ingredient_counter()

        with allure.step("Добавление ингредиента в заказ"):
            main_page.add_ingredient_to_order()

        with allure.step("Проверка увеличения счётчика"):
            assert main_page.get_ingredient_counter() > initial_count


@allure.feature("Основной функционал")
@allure.story("Оформление заказа")
class TestOrder:
    @allure.title("Тест отправки заказа")
    def test_order_submission(self, browser, test_user):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        with allure.step("Открытие страницы логина"):
            login_page.open_url("https://stellarburgers.nomoreparties.site/login")

        with allure.step("Авторизация пользователя"):
            login_page.input_email(test_user["user"]["email"])
            login_page.input_password(test_user["user"]["password"])
            login_page.click_login()

        with allure.step("Добавление ингредиента и оформление заказа"):
            main_page.add_ingredient_to_order()
            main_page.submit_order()
            assert main_page.is_order_successful()
