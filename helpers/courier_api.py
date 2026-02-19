import requests
from helpers.endpoints import BASE_API_URL

def create_courier(payload):
    return requests.post(f"{BASE_API_URL}/courier", data = payload)

def login_courier(payload):
    return requests.post(f"{BASE_API_URL}/courier/login", data = payload)

def create_order(payload):
    return requests.post(f"{BASE_API_URL}/orders", json = payload)

def get_orders():
    return requests.get(f"{BASE_API_URL}/orders")

def delete_courier(courier_id):
    return requests.delete(f"{BASE_API_URL}/courier/{courier_id}")
