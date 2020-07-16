import pytest

from test.src.intsight_test.test_infra.api.base_test_classes.base_github_gist_test import BaseGithubGistTest


@pytest.mark.system_tests
class TestGithubGist(BaseGithubGistTest):
    def test_github_gist(self):
        self.init_all_test_variables()
        # Listing user gists
        base_user_gists_list = self.get_user_gists()
        # create new user gist
        user_gist = self.create_user_gist()
        updated_user_gists = self.get_user_gists()
        assert len(updated_user_gists) == len(base_user_gists_list) + 1
        # edit newly created gist - updating the description
        user_gist.description = "new_description"
        self.update_user_gist_data(user_gist)
        updated_gist = self.get_gist_by_id(user_gist.id)
        # validating that data was updated successfully
        assert updated_gist.description == "new_description"
        # get previous revision of gist
        gist_previous_revision = self.get_gist_previous_revision(user_gist)
        self.validate_gist_details(gist_previous_revision, updated_gist)
        # star a gist
        self.star_gist(user_gist.id)
        # delete a gist
        self.delete_gist(user_gist.id)
        # delete the newly created gist and validate len of lists
        updated_user_gists = self.get_user_gists()
        assert len(updated_user_gists) == len(base_user_gists_list)
        # add a fetching by id and validate it's not successful
