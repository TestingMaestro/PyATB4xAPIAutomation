import pytest


@pytest.mark.smoke(reason="Smoke P1 TC")
class Test_CRUD(object):

    def test_update_req1(self):
        assert True == True

    def test_update_req2(self):
        assert False == True
