from test.src.intsight_test.test_infra.api.api_client import ApiClient


class BaseApiTest:
    api_client = None

    def init_all_test_variables(self):
        self.api_client = ApiClient()
