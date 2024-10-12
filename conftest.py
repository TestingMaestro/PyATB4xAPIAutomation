import pytest
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    load_dotenv()
    user_name = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": user_name,
        "password": password
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(f"Token = {token}")
    return token


@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking"
    URL = base_url + path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Yashodhar",
        "lastname": "Karki",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_json = requests.post(url=URL, headers=headers, json=json_payload)
    assert response_json.status_code == 200
    booking_id = response_json.json()["bookingid"]
    print(booking_id)
    return booking_id


@pytest.fixture()
def read_excel_csv():
    pass


@pytest.fixture()
def read_sql_file_database():
    pass


@pytest.fixture()
def launch_browser():
    print("Launching Browser")
    return "chrome"


@pytest.fixture()
def close_browser():
    print("Launching Browser")
    return "closed"
