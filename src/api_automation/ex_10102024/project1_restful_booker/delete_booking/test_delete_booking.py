import pytest
import requests
import allure
from src.api_automation.ex_10102024.project1_restful_booker.b_update_booking import \
    test_update_booking_put_patch as tokengen

# DELETE Request
# URL, Token, Headers, Payload
token = tokengen.create_token()


# def create_token():
#     URL = "https://restful-booker.herokuapp.com/auth"
#     headers = {"Content-Type": "application/json"}
#     json_payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     response = requests.post(url=URL, headers=headers, json=json_payload)
#     token = response.json()["token"]
#     print(f"Token = {token}")
#     return token

@allure.title("Test DELETE Request - Delete a Booking[Positive]")
@allure.description(
    "TC #1 - Verify that via DELETE request bookings should be deleted valid response is received with 404 not status "
    "code"
    "received")
@allure.tag("Smoke", "P0")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#1")
@pytest.mark.crud
def test_delete_booking():
    url = "https://restful-booker.herokuapp.com/booking/919"
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response = requests.delete(url=url, headers=headers)
