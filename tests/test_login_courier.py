import allure
from helpers.courier_api import create_courier, login_courier

class TestLoginCourier:
    @allure.story("Логин курьера")
    @allure.title("Авторизация курьера с валидными учётными данными")
    @allure.description(
    "Создаётся курьер, затем выполняется логин с корректным логином и паролем."
    "Ожидается статус 200 и наличие id в ответе."
    )    
    def test_login_courier_with_valid_credentials_returns_id(self, courier_data):
        create_courier(courier_data)
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.story("Логин курьера")
    @allure.title("Проверка возврата ошибки при авторизации курьера без указания логина")
    @allure.description(
    "Создаётся курьер, затем выполняется логин без заполнения поля login."
    "Ожидается статус 400 и сообщение 'Недостаточно данных для входа'."
    )
    def test_login_courier_without_login_returns_400(self, courier_data):
        create_courier(courier_data)
        payload = {
            "password": courier_data["password"]
        }
        response = login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.story("Логин курьера")
    @allure.title("Проверка возврата ошибки при авторизации курьера с указанием неверного пароля")
    @allure.description(
    "Создаётся курьер, затем выполняется логин c неверным паролем."
    "Ожидается статус 404 и сообщение 'Учетная запись не найдена'."
    )
    def test_login_courier_with_wrong_password_returns_404(self, courier_data):
        create_courier(courier_data)
        payload = {
            "login": courier_data["login"],
            "password": 'WrongPassword123'
        }

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.story("Логин курьера")
    @allure.title("Проверка возврата ошибки при авторизации под несуществующим пользователем")
    @allure.description(
    "Авторизация с учетными данными, которых нет в системе."
    "Ожидается статус 404 и сообщение 'Учетная запись не найдена'."
    )
    def test_login_non_existing_user_returns_404(self):
        payload = {
            "login": 'User_753',
            "password": 'WrongPassword123'
        }
        response = login_courier(payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
