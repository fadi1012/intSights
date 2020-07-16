from test.src.intsight_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


class GistFile:
    def __init__(self, gist_file_data):
        self.gist_file_data = gist_file_data

    def to_dict(self):
        return {self.gist_file_data.filename: self.gist_file_data.__dict__}


class GistFileData:
    def __init__(self, filename, type, language, raw_url, size):
        self.filename = filename
        self.type = type
        self.language = language
        self.raw_url = raw_url
        self.size = size


class CreateGistFileRequest:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content


class CreateGistRequest:
    def __init__(self, description, public, files):
        self.description = description
        self.public = public
        self.files = files

    def to_dict(self):
        files_dict = GistFile(self.files[0]).to_dict()
        return {'description': self.description, 'public': self.public, 'files': files_dict}


class UserGist:
    def __init__(self, description, public, files, id=None, version=None):
        self.description = description
        self.public = public
        self.files = files
        self.id = id
        self.version = version

    @staticmethod
    def generate_default_user_gist_data():
        description = "test" + str(get_rand_number_between_zero_to_max_number(100, 10))
        files = [CreateGistFileRequest(filename="test-user-gist" + str(get_rand_number_between_zero_to_max_number(100, 10)) + '.txt', content="hello world!")]
        return CreateGistRequest(description=description, public=True, files=files)

    def to_dict(self):
        files_dict = GistFile(self.files[0]).to_dict()
        return {'description': self.description, 'public': self.public, 'files': files_dict}
