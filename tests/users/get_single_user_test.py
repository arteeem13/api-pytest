import requests

from configurations.constants import BASE_URL, BASE_PATH_SINGLE_USER
from src.base_classes.jsonschema_validate_response import Response
from src.schemas.json_schemas.get_single_user import SINGLE_USER_SCHEMA


def test_check_response_with_jsonschema():
    response = requests.get(url=BASE_URL + BASE_PATH_SINGLE_USER)
    response_data = Response(response)
    response_data.assert_status_code(200).validate_json_schema(SINGLE_USER_SCHEMA)

