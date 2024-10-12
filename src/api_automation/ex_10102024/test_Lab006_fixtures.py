# Fixtures
# used in Test case context
# Similar to  - pre and post-condition
# what should be executed before sending the request and after sending the request

# precondition for update booking - token, booking id

import pytest


@pytest.fixture()
def is_married():
    return True


# consuming in the testcase
def test_consume(is_married):
    assert is_married == True
