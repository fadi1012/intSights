from test.src.intsight_test.test_infra.utilities.http_client import HttpClient


class ApiClient:
    def __init__(self):
        self.__http_client = HttpClient()