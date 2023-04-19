import requests

from configurations.constants import BASE_URL, BASE_PATH_SINGLE_RESOURCE
from src.schemas.pydantic_schemas.get_single_resource import ModelSingleResource
from src.base_classes.single_resource_validate_response import Response


def test_check_response_with_pydantic_schema():
    response = requests.get(url=BASE_URL + BASE_PATH_SINGLE_RESOURCE)
    response_data = Response(response)
    response_data.assert_status_code(200).validate_pydantic_schema(ModelSingleResource)
