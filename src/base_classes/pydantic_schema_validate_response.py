class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate_pydantic_schema(self, schema):
        schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        assert self.response_status_code == status_code, self
        return self

    def __str__(self):
        return f"\nRequest URL: {self.response.url} \n"\
               f"Response status code: {self.response.status_code} \n"\
               f"Response body: {self.response_json}"
