import requests
import allure
from data.urls import BASE_URL


class ApiHelpers:
    @allure.step("Создание тестового пользователя с email: {email}")
    def create_test_user(self, email, password):
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={"email": email, "password": password, "name": "Test User"}
        )
        if response.status_code != 200:
            raise Exception(f"Не удалось создать пользователя: {response.json()}")
        return response.json()

    @allure.step("Удаление тестового пользователя с токеном доступа")
    def delete_test_user(self, access_token):
        """Удаляет тестового пользователя через API"""
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.delete(f"{BASE_URL}/auth/user", headers=headers)
        if response.status_code != 200:
            raise Exception(f"Не удалось удалить пользователя: {response.json()}")

    @allure.step("Авторизация тестового пользователя с email: {email}")
    def login_test_user(self, email, password):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": email, "password": password}
        )
        if response.status_code != 200:
            raise Exception(f"Не удалось авторизоваться: {response.json()}")
        return response.json()["accessToken"]

    @staticmethod
    @allure.step("Создание заказа с ингредиентами: {ingredients}")
    def create_order(token, ingredients):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
