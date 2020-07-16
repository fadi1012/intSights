import pytest


# test ticket : https://colabo.atlassian.net/browse/BUZZ-3496
@pytest.mark.system_tests
class TestPoc():
    def test_poc(self):
        self.init_all_test_variables()
