from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and @href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and @class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
