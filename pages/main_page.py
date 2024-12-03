from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_constructor(self):
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def click_feed(self):
        self.driver.find_element(*MainPageLocators.FEED_BUTTON).click()

    def click_ingredient(self):
        self.driver.find_element(*MainPageLocators.FIRST_INGREDIENT).click()

    def close_popup(self):
        self.driver.find_element(*MainPageLocators.CLOSE_POPUP_BUTTON).click()

    def add_ingredient_to_order(self):
        ingredient = self.driver.find_element(*MainPageLocators.FIRST_INGREDIENT)
        order_area = self.driver.find_element(*MainPageLocators.ORDER_AREA)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, order_area).perform()

    def get_ingredient_counter(self):
        counter = self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    def submit_order(self):
        self.driver.find_element(*MainPageLocators.SUBMIT_ORDER_BUTTON).click()

    def is_order_successful(self):
        return self.driver.find_element(*MainPageLocators.ORDER_SUCCESS_MESSAGE).is_displayed()

    def is_popup_visible(self):
        try:
            popup = self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_POPUP)
            return popup.is_displayed()
        except NoSuchElementException:
            return False
