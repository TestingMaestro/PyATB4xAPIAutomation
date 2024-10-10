import pytest
import requests
import allure


@allure.title("Test GET Request - valid booking id [Positive]")
@allure.description(
    "TC #1 - Verify that via GET valid response is received with 200Ok status code "
    "received")
@allure.tag("Smoke", "P0", "Valid Booking id")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_booking_id():
    test_url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(test_url)
    print(response_data.text, end="\n")  # to get the response in text format and prints in the terminal console
    print(response_data.json())  # to get the Json response
    print(response_data.headers)  # to get the header info and prints in the terminal console
    assert response_data.status_code == 200, f"expected status code is 200 but got {response_data.status_code}"


@allure.title("Test GET Request - Negative booking id")
@allure.description(
    "TC #2 - Verify that via GET 404 Not found status code should be shown for negative booking ids")
@allure.tag("Smoke", "P0", "Invalid Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_negative_booking_():
    test_url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(test_url)
    print(response_data.text, end="\n")  # to get the response in text format and prints in the terminal console
    assert response_data.status_code == 404, f"expected status code is 404 but got {response_data.status_code}"


@allure.title("Test GET Request - Booking id is null")
@allure.description(
    "TC #3 - Verify that via GET 404 Not found status code should be shown when the booking id is null")
@allure.tag("Smoke", "P0", "Invalid Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_booking_id_null():
    test_url = "https://restful-booker.herokuapp.com/booking/null"
    response_data = requests.get(test_url)
    print(response_data.text, end="\n")  # to get the response in text format and prints in the terminal console
    assert response_data.status_code == 404, f"expected status code is 404 but got {response_data.status_code}"


@allure.title("Test GET Request - Booking id is empty")
@allure.description(
    "TC #4 - Verify that via GET 404 Not found status code should be shown when the booking id is empty")
@allure.tag("Smoke", "P0", "Invalid Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_single_booking_empty():
    test_url = "https://restful-booker.herokuapp.com/booking/ "
    response_data = requests.get(test_url)
    print(response_data.text, end="\n")  # to get the response in text format and prints in the terminal console
    assert response_data.status_code == 404, f"expected status code is 404 but got {response_data.status_code}"


@allure.title("Test GET Request - Non-existing booking id")
@allure.description(
    "TC #5 - Verify that via GET 404 Not found status code should be shown when the booking id is null")
@allure.tag("Smoke", "P0", "Invalid Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#5")
@pytest.mark.smoke
def test_get_single_booking_id_non_existing():
    test_url = "https://restful-booker.herokuapp.com/booking/10000"
    response_data = requests.get(test_url)
    print(response_data.text, end="\n")  # to get the response in text format and prints in the terminal console
    assert response_data.status_code == 404, f"expected status code is 404 but got {response_data.status_code}"


@allure.title("Test GET Request - Booking id with special characters")
@allure.description(
    "TC #6 - Verify that via GET 404 Not found status code should be shown when the booking id with special characters")
@allure.tag("Smoke", "P0", "Invalid Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#6")
@pytest.mark.smoke
def test_get_single_booking_id_specialchars():
    test_url = "https://restful-booker.herokuapp.com/booking/@$$"
    response_data = requests.get(test_url)
    print(response_data.text, end="\n")  # to get the response in text format and prints in the terminal console
    assert response_data.status_code == 404, f"expected status code is 404 but got {response_data.status_code}"
