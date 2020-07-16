class GistFile:
    def __init__(self, gist_file_data, index):
        self.gist_file_data =  gist_file_data
        self.index = index

    def to_dict(self):
        return {'gistfile' + str(self.index) + '.text' : self.gist_file_data.__dict__}

class GistFileData:
    def __init__(self, filename, type, language, raw_url, size):
        self.filename = filename
        self.type = type
        self.language = language
        self.raw_url = raw_url
        self.size = size


class UserGist:
    def __init__(self, description, public, files, id=None, version=None):
        self.description = description
        self.public = public
        self.files = files
        self.id = id
        self.version = version

    @staticmethod
    def generate_default_user_gist_data():
        return UserGist(description="test", public=True, files=[GistFileData(filename="test-user-gist", type="text/plain", language="Text",
                                                                             raw_url="https://gist.githubusercontent.com/fadiMawsouq/4670b77e7e7e72fad048dd683e7e0758/raw/30d74d258442c7c65512eafab474568dd706c430/gistfile1.txt",
                                                                             size=4)])

    def to_dict(self):
        files_dict = [GistFile(file, index).to_dict() for index, file in enumerate(self.files, start=1)]
        return {'description': self.description, 'public': self.public, 'files': files_dict}
