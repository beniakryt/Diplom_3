import pytest
import requests
from selenium import webdriver
import time
import random
import string

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def debug_pause(seconds=1):
    time.sleep(seconds)

class FirefoxDriverWithPause(webdriver.Firefox):
    def find_element(self, *args, **kwargs):
        element = super().find_element(*args, **kwargs)
        debug_pause(1)
        return element

    def click(self, *args, **kwargs):
        super().click(*args, **kwargs)
        debug_pause(1)

    def send_keys(self, *args, **kwargs):
        super().send_keys(*args, **kwargs)
        debug_pause(1)

def generate_random_email():
    domain = "example.com"
    prefix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}@{domain}"

def generate_random_name():
    return "User_" + "".join(random.choices(string.ascii_letters, k=5))

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = FirefoxDriverWithPause()
        driver.is_firefox = True
        driver.implicitly_wait(10)

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def test_user():
    test_user_data = {
        "email": generate_random_email(),
        "password": "test_password123",
        "name": generate_random_name()
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=test_user_data)
    if response.status_code not in (200, 201):
        pytest.fail(f"Failed to create test user: {response.json()}")

    auth_response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    })
    if auth_response.status_code != 200:
        pytest.fail(f"Failed to authenticate test user: {auth_response.json()}")

    tokens = auth_response.json()
    yield {
        "user": test_user_data,
        "tokens": tokens
    }

    headers = {"Authorization": tokens["accessToken"]}
    delete_response = requests.delete(f"{BASE_URL}/auth/user", headers=headers)
    if delete_response.status_code != 200:
        print(f"Failed to delete test user: {delete_response.json()}")
