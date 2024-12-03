from locators.personal_account_locators import PersonalAccountLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_personal_account(self):
        self.driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()

    def go_to_order_history(self):
        # Клик по кнопке "История заказов"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.ORDER_HISTORY_SECTION)
        ).click()

    def logout(self):
        """Выход из аккаунта"""
        self.driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()

