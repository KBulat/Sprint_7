BASE_URL = "https://qa-scooter.praktikum-services.ru/"
BASE_API_URL = f"{BASE_URL}/api/v1"

class Endpoints:
    courier_create = f"{BASE_API_URL}/courier" # Создание курьера
    courier_login = f"{BASE_API_URL}/courier/login" # Логин курьера в системе
    orders = f"{BASE_API_URL}/orders" # Получение списка заказов
