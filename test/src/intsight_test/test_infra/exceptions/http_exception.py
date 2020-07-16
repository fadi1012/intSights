class HttpException(Exception):
    def __init__(self, status_code, error_id, error_text, original_error_text):
        Exception.__init__(self, error_text)
        self.status_code = status_code
        self.error_id = error_id
        self.error_text = error_text
        self.original_error_text = original_error_text