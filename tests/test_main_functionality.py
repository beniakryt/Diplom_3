import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.feature("Основной функционал")
@allure.story("Переходы")
def test_constructor_navigation(browser):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    main_page = MainPage(browser)
    main_page.click_constructor()
    assert "https://stellarburgers.nomoreparties.site" in browser.current_url

@allure.feature("Основной функционал")
@allure.story("Переходы")
def test_feed_navigation(browser):
    browser.get("https://stellarburgers.nomoreparties.site")
    main_page = MainPage(browser)
    main_page.click_feed()
    assert "feed" in browser.current_url

@allure.feature("Основной функционал")
@allure.story("Работа с ингредиентами")
def test_ingredient_details_popup_open(browser):
    browser.get("https://stellarburgers.nomoreparties.site")
    main_page = MainPage(browser)
    main_page.click_ingredient()
    assert main_page.is_popup_visible()

@allure.feature("Основной функционал")
@allure.story("Работа с ингредиентами")
def test_ingredient_details_popup_close(browser):
    browser.get("https://stellarburgers.nomoreparties.site")
    main_page = MainPage(browser)
    main_page.click_ingredient()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    )
    main_page.close_popup()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    )
    assert not main_page.is_popup_visible()

@allure.feature("Основной функционал")
@allure.story("Добавление ингредиентов")
def test_ingredient_counter_increase(browser):
    browser.get("https://stellarburgers.nomoreparties.site")
    main_page = MainPage(browser)
    initial_count = main_page.get_ingredient_counter()
    main_page.add_ingredient_to_order()
    WebDriverWait(browser, 10).until(
        lambda driver: main_page.get_ingredient_counter() > initial_count
    )
    assert main_page.get_ingredient_counter() > initial_count

@allure.feature("Основной функционал")
@allure.story("Оформление заказа")
def test_order_submission(browser, test_user):
    browser.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(browser)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    login_page.input_email(test_user["user"]["email"])
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
    )
    login_page.input_password(test_user["user"]["password"])
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    login_page.click_login()
    main_page = MainPage(browser)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(MainPageLocators.FIRST_INGREDIENT)
    )
    main_page.add_ingredient_to_order()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(MainPageLocators.SUBMIT_ORDER_BUTTON)
    )
    main_page.submit_order()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_SUCCESS_MESSAGE)
    )
    assert main_page.is_order_successful()
