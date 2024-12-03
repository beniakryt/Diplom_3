from selenium.webdriver.common.by import By

class LoginPageLocators:
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")
    RECOVER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']")
    TOGGLE_PASSWORD_BUTTON = (By.XPATH, "//div[@class = 'input__icon input__icon-action']")
    TOGGLE_PASSWORD_BUTTON_ACTIVE = (By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_status_active')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти')]")