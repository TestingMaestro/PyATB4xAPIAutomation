# Verify create booking

# verify booking id is not null,
# status code,
# response headers, response body, key data type in response,firstname

import pytest
import requests
import allure


@allure.title("Test GET Request - RestFul booker Project #1")
@allure.description(
    "TC #1 - Verify that GET request is able to provide the single booking details and verify that valid response is "
    "received")
@allure.tag("Smoke", "P0", "Single Booking")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_booking_id():
    test_url = "https://restful-booker.herokuapp.com/booking/123"
    response_data = requests.get(test_url)
    print(response_data.text,end="\n")  # to get the response in text format and prints in the terminal console
    print(response_data.json())  # to get the Json response
    print(response_data.headers)  # to get the header info and prints in the terminal console
    assert response_data.status_code == 200, f"expected status code is 200 but got {response_data.status_code}"
