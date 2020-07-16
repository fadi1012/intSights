from test.src.intsight_test.test_infra.api.case_classes.user_gist import GistFileData, UserGist
from test.src.intsight_test.test_infra.conf import config
from test.src.intsight_test.test_infra.utilities.http_client import HttpClient


class ApiClient:
    def __init__(self):
        self.__http_client = HttpClient()
        self.token = "025cdddd7d82ae54d3bccd6c2a9c5e538aca9d65"
        self._oauth_token = {"Authorization": "bearer " + self.token}

    def __generate_user_gist_files(self, params):
        user_gists_files = []
        for index in enumerate(params, start=1):
            gistfile = params['gistfile' + str(index[0]) + '.txt']
            user_gists_files.append(GistFileData(filename=gistfile['filename'], type=gistfile['type'], language=gistfile['language'], raw_url=gistfile['raw_url'], size=gistfile['size']))
        return user_gists_files

    def __generate_user_gist(self, params):
        files = self.__generate_user_gist_files(params=params['files'])
        return UserGist(public=params['public'], description=params['description'], files=files, id=params['id'], version=params['version'] if 'version' in params else None)

    def get_user_gist_files(self):
        resp = self.__http_client.get(url=config.USER_GISTS,
                                      headers=self._oauth_token)
        return self.__generate_user_gist_files(params=resp[0]['files'])

    def get_user_gists(self):
        resp = self.__http_client.get(url=config.USER_GISTS,
                                      headers=self._oauth_token)
        return [self.__generate_user_gist(params=item) for item in resp]

    def create_user_gist(self, user_gist_data):
        resp = self.__http_client.post(url=config.USER_GISTS,
                                       data=user_gist_data.to_dict(), headers=self._oauth_token)

        return self.__generate_user_gist(params=resp)

    def update_user_gist_data(self, user_gist_data):
        return self.__http_client.post(url=config.UPDATE_USER_GIST.format(user_gist_data.id),
                                       data=user_gist_data.to_dict(), headers=self._oauth_token)

    def get_gist_by_id(self, gist_id):
        resp = self.__http_client.get(url=config.UPDATE_USER_GIST.format(gist_id),
                                      headers=self._oauth_token)
        return self.__generate_user_gist(params=resp)

    def get_gist_previous_revision(self, gist_id, gist_version):
        resp = self.__http_client.get(url=config.GET_USER_GIST_REVISION.format(gist_id, gist_version),
                                      headers=self._oauth_token)
        return self.__generate_user_gist(params=resp)

    def star_gist(self, gist_id):
        return self.__http_client.put(url=config.STAR_GIST.format(gist_id), headers=self._oauth_token, data={})

    def delete_gist(self, gist_id):
        return self.__http_client.delete(url=config.DELETE_GIST.format(gist_id), headers=self._oauth_token)
