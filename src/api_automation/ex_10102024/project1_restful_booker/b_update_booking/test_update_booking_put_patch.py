# Put Request
# URL
# Token
# headers
# payload
import pytest
import requests
import allure


# create a token
def create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(f"Token = {token}")
    return token


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


@allure.title("Test PUT Request - Update Booking[Positive]")
@allure.description(
    "TC #1 - Verify that via PUT update booking provides valid response is received with 200 Ok status code "
    "received")
@allure.tag("Smoke", "P0", "Valid Booking id")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#1")
@pytest.mark.crud
def test_update_booking_put():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    URL = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Meow",
        "lastname": "T",
        "totalprice": 92,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-09-28",
            "checkout": "2024-10-31"
        },
        "additionalneeds": "Lunch Only"

    }
    response = requests.put(url=URL, headers=headers, json=json_payload)
    print(response.text)
    assert response.status_code == 200, f"expected is 200, but got {response.status_code}"
    assert response.json()["firstname"] == "Meow"


@allure.title("Test PATCH Request - Update Booking[Positive]")
@allure.description(
    "TC #2 - Verify that via PUT updating first and lastname in booking provides valid response is received with 200 "
    "Ok status code"
    "received")
@allure.tag("Smoke", "P0", "Valid TC")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#2")
@pytest.mark.crud
def test_update_booking_patch():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    URL = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Souparnika",
        "lastname": "Karki",
        "bookingdates": {
            "checkin": "2018-09-29",
            "checkout": "2019-09-23"
        }
    }
    response = requests.patch(url=URL, headers=headers, json=json_payload)
    print(response.text)
    assert response.status_code == 200, f"expected is 200, but got {response.status_code}"
    firstname = response.json()["firstname"]
    lastname = response.json()["lastname"]
    print(type(firstname))
    print(type(lastname))
    assert firstname == "Souparnika", f"expected is Souparnika, but got {firstname}"
    assert lastname == "Karki", f"expected is Karki, but got {lastname}"
