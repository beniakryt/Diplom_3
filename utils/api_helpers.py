import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def create_test_user(email, password):
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"email": email, "password": password, "name": "Test User"}
    )
    if response.status_code != 200:
        raise Exception(f"Не удалось создать пользователя: {response.json()}")
    return response.json()

def delete_test_user(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete(f"{BASE_URL}/auth/user", headers=headers)
    if response.status_code != 200:
        raise Exception(f"Не удалось удалить пользователя: {response.json()}")

def login_test_user(email, password):
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email, "password": password}
    )
    if response.status_code != 200:
        raise Exception(f"Не удалось авторизоваться: {response.json()}")
    return response.json()["accessToken"]

class ApiHelpers:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    @staticmethod
    def create_order(token, ingredients):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f"{ApiHelpers.BASE_URL}/orders", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()