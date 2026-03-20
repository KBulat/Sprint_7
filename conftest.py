import pytest
from helpers.generator import generate_courier_payload
from helpers.courier_api import login_courier, delete_courier

@pytest.fixture
def courier_payload():
    return generate_courier_payload()
   
@pytest.fixture
def courier_data():
    data = generate_courier_payload()

    yield data

    credentials = {
        "login": data["login"],
        "password": data["password"]
    }

    login_response = login_courier(credentials)

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        if courier_id:
            delete_courier(courier_id)
