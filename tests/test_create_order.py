import allure
import pytest
from helpers.courier_api import create_order
from helpers.order import order_data

class TestCreateOrder:
    @allure.story("Создание заказа")
    @allure.title("Создание заказа с разными вариантами цвета самоката")
    @allure.description(
    "Отправляется запрос на создание заказа с разными вариантами цвета самоката."
    "Ожидается статус 201 и наличие track в ответе."
    )
    @pytest.mark.parametrize("color", [
        ['BLACK'], 
        ['GREY'], 
        ['BLACK, GREY'], 
        None
    ])
    def test_create_order_with_color_options_returns_201(self, color):
        payload = order_data.copy()

        if color is not None:
            payload['color'] = color

        response = create_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()
