import pytest


@pytest.fixture()
def create_token():
    return "abc"


@pytest.fixture()
def create_booking_id():
    return 1


@pytest.fixture()
def read_excel_file():
    return "excel"


@pytest.fixture()
def read_json_file():
    return "{}"


# consuming in the test
def test_consume(create_token, create_booking_id, read_json_file, read_excel_file):
    print(create_booking_id)
    print(create_token)
    print(read_json_file)
    print(read_excel_file)
