import pytest
import requests
from selenium import webdriver
from data.urls import BASE_URL
from utils.helpers import generate_random_email, generate_random_name


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

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
