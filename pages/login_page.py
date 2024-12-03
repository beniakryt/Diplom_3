from locators.login_page_locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_password_recovery(self):
        self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD_BUTTON).click()

    def input_email(self, email):
        email_field = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

    def click_recover(self):
        self.driver.find_element(*LoginPageLocators.RECOVER_BUTTON).click()

    def toggle_password_visibility(self):
        self.driver.find_element(*LoginPageLocators.TOGGLE_PASSWORD_BUTTON).click()

    def is_field_active(self):
        field_div = self.driver.find_element(*LoginPageLocators.TOGGLE_PASSWORD_BUTTON_ACTIVE)
        field_class = field_div.get_attribute("class")
        return "input_status_active" in field_class

    def input_password(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()