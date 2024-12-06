from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FEED_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_FEED_ITEM_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    ORDER_COMPLETED_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    ORDER_LIST_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]")
    ORDER_LIST_IN_FEED = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']//p[contains(@class, 'text_type_digits-default')]")

    ORDER_DETAILS_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")
    ORDER_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
