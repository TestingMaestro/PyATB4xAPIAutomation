import pytest
import allure
import requests


@allure.title("Test POST Request - Create a Booking with empty payload")
@allure.description(
    "TC #1 - Verify that empty payload is sent via post request and response received is 500")
@pytest.mark.crud
def test_create_booking_negative_tests_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking"
    headers = {"Content-Type": "application/json"}
    URL = base_url + path
    json_payload = {}

    response_json = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response_json.status_code == 500


@allure.title("Test POST Request - Create a Booking with empty payload")
@allure.description(
    "TC #2 - Verify the booking with total price is string negative")
@pytest.mark.crud
def test_create_booking_negative_tests_tc2():  # Bug needs to be raised
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking"
    headers = {"Content-Type": "application/json"}
    URL = base_url + path
    json_payload = {
        "firstname": "Yashodhar",
        "lastname": "A Karki",
        "totalprice": "Yash",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_json = requests.post(url=URL, headers=headers, json=json_payload)
    assert response_json.status_code == 500


@allure.title("Test POST Request - Create a Booking with checking dates to future century dates")
@allure.description(
    "TC #3 - Verify the booking with checkin date's year to max number")
@pytest.mark.crud
def test_create_booking_negative_tests_tc3():  # Bug needs to be raised
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking"
    headers = {"Content-Type": "application/json"}
    URL = base_url + path
    json_payload = {
        "firstname": "Yashodhar",
        "lastname": "A Karki",
        "totalprice": "Yash",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "5000-01-01", # we need to check with PMT
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_json = requests.post(url=URL, headers=headers, json=json_payload)
    assert response_json.status_code == 500
