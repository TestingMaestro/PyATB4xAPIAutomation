import pytest
import requests
import allure


@allure.title("Test PUT Request - Update Booking[Positive]")
@allure.description(
    "TC #1 - Verify that via PUT update booking provides valid response is received with 200 Ok status code "
    "received")
@allure.tag("Smoke", "P0", "Valid Booking id")
@allure.severity(allure.severity_level.CRITICAL)\
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#1")
@pytest.mark.crud
def test_update_req1(create_token, create_booking):
    print("Token: ", create_token)
    print("Booking ID", create_booking)
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking/" + str(create_booking)
    URL = base_url + path_url
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    json_payload = {

        "firstname": "MeowSou",
        "lastname": "TM",
        "totalprice": 922,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-09-28",
            "checkout": "2026-10-31"
        },
        "additionalneeds": "Dinner Only"

    }

    json_response = requests.put(url=URL, headers=headers, json=json_payload)
    assert json_response.json()[
               "firstname"] == "MeowSou", f"expected is MeowSou then got {json_response.json()["firstname"]}"
    assert json_response.status_code == 200, f"expected is MeowSou then got {json_response.st}"
