# create booking
# URL
# headers
# body--> Json
# path param
# query param
import jsonschema.exceptions
import pytest
import requests
import allure
from jsonschema import validate


@allure.title("Test GET Request - Create a Booking")
@allure.description(
    "TC #6 - Verify that via POST request booking should be created successfully and response should be 201")
@allure.tag("Smoke", "P0", "Valid Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yashodhar Karki")
@allure.testcase("TC#7")
@pytest.mark.crud
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com/booking"
    request_headers = {"Content-Type": "application/json"}
    request_body = {
        "firstname": "Yashodhar ",
        "lastname": "A Karki",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates":
            {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
        "additionalneeds": "Breakfast"

    }
    schema = {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "http://example.com/example.json",
        "type": "object",
        "default": {},
        "title": "Root Schema",
        "required": [
            "bookingid",
            "booking"
        ],
        "properties": {
            "bookingid": {
                "type": "integer",
                "default": 0,
                "title": "The bookingid Schema",
                "examples": [
                    2082
                ]
            },
            "booking": {
                "type": "object",
                "default": {},
                "title": "The booking Schema",
                "required": [
                    "firstname",
                    "lastname",
                    "totalprice",
                    "depositpaid",
                    "bookingdates",
                    "additionalneeds"
                ],
                "properties": {
                    "firstname": {
                        "type": "string",
                        "default": "",
                        "title": "The firstname Schema",
                        "examples": [
                            "Yashodhar"
                        ]
                    },
                    "lastname": {
                        "type": "string",
                        "default": "",
                        "title": "The lastname Schema",
                        "examples": [
                            "A Karki"
                        ]
                    },
                    "totalprice": {
                        "type": "integer",
                        "default": 0,
                        "title": "The totalprice Schema",
                        "examples": [
                            300
                        ]
                    },
                    "depositpaid": {
                        "type": "boolean",
                        "default": False,
                        "title": "The depositpaid Schema",
                        "examples": [
                            True
                        ]
                    },
                    "bookingdates": {
                        "type": "object",
                        "default": {},
                        "title": "The bookingdates Schema",
                        "required": [
                            "checkin",
                            "checkout"
                        ],
                        "properties": {
                            "checkin": {
                                "type": "string",
                                "default": "",
                                "title": "The checkin Schema",
                                "examples": [
                                    "2018-01-01"
                                ]
                            },
                            "checkout": {
                                "type": "string",
                                "default": "",
                                "title": "The checkout Schema",
                                "examples": [
                                    "2019-01-01"
                                ]
                            }
                        },
                        "examples": [{
                            "checkin": "2018-01-01",
                            "checkout": "2019-01-01"
                        }]
                    },
                    "additionalneeds": {
                        "type": "string",
                        "default": "",
                        "title": "The additionalneeds Schema",
                        "examples": [
                            "Breakfast"
                        ]
                    }
                },
                "examples": [{
                    "firstname": "Yashodhar",
                    "lastname": "A Karki",
                    "totalprice": 300,
                    "depositpaid": True,
                    "bookingdates": {
                        "checkin": "2018-01-01",
                        "checkout": "2019-01-01"
                    },
                    "additionalneeds": "Breakfast"
                }]
            }
        },
        "examples": [{
            "bookingid": 2082,
            "booking": {
                "firstname": "Yashodhar",
                "lastname": "A Karki",
                "totalprice": 300,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2018-01-01",
                    "checkout": "2019-01-01"
                },
                "additionalneeds": "Breakfast"
            }
        }]
    }

    response_data = requests.post(url=base_url, headers=request_headers, json=request_body)
    print(response_data.json())
    response_time = response_data.elapsed.total_seconds()
    print("Time of Response received", response_time)
    booking_id = response_data.json()["bookingid"]
    print(booking_id)
    firstname = response_data.json()["booking"]["firstname"]
    print(firstname)
    lastname = response_data.json()["booking"]["lastname"]
    print(lastname)
    totalprice = response_data.json()["booking"]["totalprice"]
    print(totalprice)
    deposit_paid = response_data.json()["booking"]["depositpaid"]
    print(deposit_paid)
    checkin_dates = response_data.json()["booking"]["bookingdates"]["checkin"]
    print(checkin_dates)
    checkout_dates = response_data.json()["booking"]["bookingdates"]["checkout"]
    print(checkout_dates)
    needs = response_data.json()["booking"]["additionalneeds"]
    print(needs)

    assert response_data.status_code == 200
    assert isinstance(booking_id, int), f"expected int but got {type(booking_id)}"
    assert booking_id > 0
    assert booking_id is not None

    assert firstname == "Yashodhar"
    assert firstname is not None

    assert lastname == "A Karki"
    assert lastname is not None

    assert deposit_paid == True
    assert deposit_paid is not None

    assert checkin_dates == "2018-01-01"
    assert checkin_dates is not None

    try:
        validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as ve:
        print(ve)
