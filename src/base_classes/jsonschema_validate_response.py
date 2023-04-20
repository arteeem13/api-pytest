from jsonschema import validate

from src.configurations.error_messages import ERROR_STATUS_CODE_MESSAGE


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate_json_schema(self, schema):
        validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        assert self.response_status_code == status_code, ERROR_STATUS_CODE_MESSAGE
        return self
