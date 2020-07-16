from test.src.intsight_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.intsight_test.test_infra.api.case_classes.user_gist import UserGist


class BaseGithubGistTest(BaseApiTest):

    def get_user_gist_files(self):
        return self.api_client.get_user_gist_files()

    def get_user_gists(self):
        return self.api_client.get_user_gists()

    def create_user_gist(self, user_gist_data=None):
        user_gist_data = user_gist_data or UserGist.generate_default_user_gist_data()
        return self.api_client.create_user_gist(user_gist_data)

    def update_user_gist_data(self, user_gist_data):
        return self.api_client.update_user_gist_data(user_gist_data)

    def get_gist_by_id(self, gist_id):
        return self.api_client.get_gist_by_id(gist_id)

    def get_gist_previous_revision(self, user_gist):
        return self.api_client.get_gist_previous_revision(user_gist.id, user_gist.version)

    def validate_gist_details(self, original_value, expected_value):
        assert original_value.description == expected_value.description
        assert original_value.id == expected_value.id
        assert original_value.public == expected_value.public
        self.validate_gist_files(original_value, expected_value)

    def validate_gist_files(self, original_value_files, expected_value_files):
        assert len(original_value_files) == len(expected_value_files)
        for index, item in enumerate(original_value_files):
            assert item == expected_value_files[index]

    def star_gist(self, gist_id):
        return self.api_client.star_gist(gist_id)

    def delete_gist(self, gist_id):
        return self.api_client.delete_gist(gist_id)
