from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Таймаут ожидания

    def click_element(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            self.force_click(locator)  # Принудительный клик через JS

    def force_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    def open_url(self, url):
        self.driver.get(url)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_text_present_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))
