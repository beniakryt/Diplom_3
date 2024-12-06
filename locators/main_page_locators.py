from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/feed']")
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @href='/ingredient/61c0c5a71d1f82001bdaaa6c' and .//p[contains(text(), 'Краторная булка N-200i')]]")
    CLOSE_POPUP_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'Modal_modal__close_modified__3V5XS') and contains(@class, 'Modal_modal__close__TnseK')]")
    ADD_TO_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Добавить')]")
    INGREDIENT_COUNTER = (By.XPATH, "(//div[@class='counter_counter__ZNLkj counter_default__28sqi']//p[@class='counter_counter__num__3nue1'])[2]")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(text(), 'Оформить заказ')]")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X') and contains(., 'идентификатор заказа')]")
    INGREDIENT_DETAILS_POPUP = (By.XPATH, "(//div[contains(@class, 'Modal_modal__container')])[1]")
    ORDER_AREA = (By.XPATH, "//span[@class='constructor-element__text' and contains(text(), 'Перетяните булочку сюда (верх)')]")