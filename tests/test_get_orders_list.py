import allure
from helpers.courier_api import get_orders

class TestGetOrdersList:
    @allure.story("Получение списка заказов")
    @allure.title("Получение полного списка заказов")
    @allure.description(
    "Отправляется запрос на получение списка заказов."
    "Ожидается статус 200 и список заказов в теле запроса."
    )
    def test_get_orders_list_returns_orders(self):
        response = get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert type(response.json()["orders"]) is list
