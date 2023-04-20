import pytest
import requests
import allure

from src.configurations.constants import BASE_URL, BASE_PATH_SINGLE_RESOURCE
from src.schemas.pydantic_schemas.single_resource import ModelSingleResource
from src.base_classes.pydantic_schema_validate_response import Response


@allure.suite('Методы resources')
@allure.title('Код ответа 200 и тело ответа соответствует json схеме при вызове /api/unknown/2')
@pytest.mark.resources_test
def test_check_response_single_resources_with_pydantic_schema():
    """Получение данных ресурса"""
    with allure.step("Вызов метода GET /api/unknown/2"):
        response = requests.get(url=BASE_URL + BASE_PATH_SINGLE_RESOURCE)

    response_data = Response(response)

    with allure.step("Код ответа 200 и тело ответа соответствует json схеме"):
        response_data.assert_status_code(200).validate_pydantic_schema(ModelSingleResource)
