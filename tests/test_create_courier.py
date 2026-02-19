import allure
from helpers.courier_api import create_courier

class TestCreateCourier:
    @allure.story("Создание курьера")
    @allure.title("Создание курьера с валидными данными")
    @allure.description(
    "Проверка создания курьера с корректным логином и паролем."
    "Ожидается статус 201 и в теле ответа запись {'ok':true}."
    )
    def test_create_courier_with_valid_data_returns_201(self, courier_payload):
        response = create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json()["ok"] is True
    
    @allure.story("Создание курьера")
    @allure.title("Проверка невозможности создания двух одинаковых курьеров")
    @allure.description(
    "Создаётся курьер, затем отправляется запрос на создание курьера с теми же данными."
    "Ожидается статус 409 и сообщение 'Этот логин уже используется. Попробуйте другой.'."
    )
    def test_create_duplicate_couriers_returns_409(self, courier_data):

        create_courier(courier_data)
        response_second = create_courier(courier_data)

        assert response_second.status_code == 409
        assert response_second.json()["message"] == "Этот логин уже используется. Попробуйте другой."
    
    @allure.story("Создание курьера")
    @allure.title("Проверка невозможности создания курьера без указания логина")
    @allure.description(
    "Отправляется запрос на создание курьера без указания логина."
    "Ожидается статус 400 и сообщение 'Недостаточно данных для создания учетной записи'."
    )
    def test_create_courier_without_login_returns_400(self, courier_payload):
        payload = courier_payload.copy()
        payload.pop("login")
        
        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.story("Создание курьера")
    @allure.title("Проверка невозможности создания курьера без указания пароля")
    @allure.description(
    "Отправляется запрос на создание курьера без указания пароля."
    "Ожидается статус 400 и сообщение 'Недостаточно данных для создания учетной записи'."
    )
    def test_create_courier_without_password_returns_400(self, courier_payload):
        payload = courier_payload.copy()
        payload.pop("password")

        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
