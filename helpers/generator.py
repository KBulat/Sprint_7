from faker import Faker

fake = Faker("ru_RU")

def generate_courier_payload():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=8, special_chars=True, digits=True),
        "firstName": fake.first_name()
    }
