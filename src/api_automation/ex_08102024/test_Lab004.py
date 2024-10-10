import pytest
import allure


@allure.title("TC#1 - Verify that 1 - 1 is equal to zero")
@allure.description("This is a smoke Test case which verifies that 1 - 1 is equal to zero")
@pytest.mark.smoke
def test_sub0():
    assert 1 - 1 == 0


@allure.title("TC#2 - Verify that 4 - 3 is equal to one")
@allure.description("This is a smoke Test case which verifies that that 4 - 3 is equal to one")
@pytest.mark.smoke
@pytest.mark.smoke
def test_sub1():
    assert 4 - 3 == 1


@allure.title("TC#3 - Verify that 2 - 1 is not equal to zero")
@allure.description("This is a smoke Test case which verifies that 2 - 1 is not equal to zero")
@pytest.mark.smoke
def test_sub2():
    assert 2 - 1 != 0


@allure.title("TC#4 - Verify that 4 - 2 is not equal to two")
@allure.description("This is a smoke Test case which verifies that 4 - 2 is not equal to two")
@pytest.mark.smoke
def test_sub3():
    assert 4 - 2 != 2


@allure.title("TC#5 - Verify that 4 - 1 is not equal to zero")
@allure.description("This is a smoke Test case which verifies that 4 - 1 is not equal to zero")
@pytest.mark.reg
def test_sub4():
    assert 4 - 1 != 0


@pytest.mark.skip(reason="This is not completed, Skip it")
def test_sub5():
    assert 1 - 1 == 0
