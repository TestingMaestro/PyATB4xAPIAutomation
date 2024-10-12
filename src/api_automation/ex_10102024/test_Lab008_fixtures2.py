import pytest


@pytest.fixture()
def create_token():
    return "abc"


@pytest.fixture()
def create_booking_id():
    return 1


def test_update_req1(create_token, create_booking_id):
    print("Token--->", create_token)
    print("Booking Id", create_booking_id)


def test_update_req2(create_token, create_booking_id):
    print("Token--->", create_token)
    print("Booking Id", create_booking_id)
