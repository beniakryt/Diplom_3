import allure
from pages.order_page import OrderPage
from utils.api_helpers import ApiHelpers


@allure.feature("Лента заказов")
@allure.story("Открытие деталей заказа")
class TestOrderDetails:
    @allure.title("Тест открытия деталей заказа")
    def test_order_details_popup(self, browser):
        order_page = OrderPage(browser)

        with allure.step("Открытие страницы ленты заказов"):
            order_page.open_feed_page()

        with allure.step("Клик по заказу в ленте"):
            order_page.click_order_feed_item()
            assert order_page.is_order_popup_visible()


@allure.feature("Лента заказов")
@allure.story("Заказы пользователя")
class TestUserOrders:
    @allure.title("Тест отображения заказа в ленте заказов")
    def test_orders_displayed_in_feed(self, browser, test_user):
        order_page = OrderPage(browser)

        with allure.step("Открытие страницы ленты заказов"):
            order_page.open_feed_page()

        with allure.step("Создание нового заказа через API"):
            ingredients = ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa73"]
            order_response = ApiHelpers.create_order(test_user["tokens"]["accessToken"], ingredients)
            new_order_number = f"#{int(order_response['order']['number']):07d}"

        with allure.step("Получение всех заказов в 'Ленте заказов'"):
            all_orders = order_page.get_all_orders_in_feed()
            assert new_order_number in all_orders


@allure.feature("Лента заказов")
@allure.story("Счётчики выполненных заказов")
class TestOrderCounters:
    @allure.title("Тест увеличения счётчика выполненных заказов за всё время")
    def test_completed_orders_all_time_increase(self, browser, test_user):
        order_page = OrderPage(browser)

        with allure.step("Открытие страницы ленты заказов"):
            order_page.open_feed_page()

        with allure.step("Получение начального значения счётчика"):
            completed_all_time = order_page.get_completed_count_all_time()

        with allure.step("Создание нового заказа через API"):
            ingredients = ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa73"]
            ApiHelpers.create_order(test_user["tokens"]["accessToken"], ingredients)

        with allure.step("Проверка увеличения счётчика 'Выполнено за всё время'"):
            order_page.wait_for_url_contains("feed")
            assert order_page.get_completed_count_all_time() > completed_all_time

    @allure.title("Тест увеличения счётчика выполненных заказов за сегодня")
    def test_completed_orders_today_increase(self, browser, test_user):
        order_page = OrderPage(browser)

        with allure.step("Открытие страницы ленты заказов"):
            order_page.open_feed_page()

        with allure.step("Получение начального значения счётчика"):
            completed_today = order_page.get_completed_count_today()

        with allure.step("Создание нового заказа через API"):
            ingredients = ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa73"]
            ApiHelpers.create_order(test_user["tokens"]["accessToken"], ingredients)

        with allure.step("Проверка увеличения счётчика 'Выполнено за сегодня'"):
            order_page.wait_for_url_contains("feed")
            assert order_page.get_completed_count_today() > completed_today


@allure.feature("Лента заказов")
@allure.story("Статус заказов")
class TestOrderStatus:
    @allure.title("Тест отображения нового заказа в разделе 'В работе'")
    def test_order_appears_in_progress(self, browser, test_user):
        order_page = OrderPage(browser)

        with allure.step("Открытие страницы ленты заказов"):
            order_page.open_feed_page()

        with allure.step("Создание нового заказа через API"):
            ingredients = ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa73"]
            order_response = ApiHelpers.create_order(test_user["tokens"]["accessToken"], ingredients)
            new_order_number = f"{int(order_response['order']['number']):07d}"

        with allure.step("Получение всех заказов в разделе 'В работе'"):
            all_orders = order_page.get_all_orders_in_progress()
            assert new_order_number in all_orders
