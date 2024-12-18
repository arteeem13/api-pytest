import allure
import pytest
import requests

from src.configurations.constants import BASE_URL, BASE_PATH_DELAYED_RESPONSE
from src.base_classes.pydantic_schema_validate_response import Response
from src.schemas.pydantic_schemas.delayed_response import ModelDelayedResponse


@allure.suite('Методы delayed response')
@allure.title('Код ответа 200 и тело ответа соответствует json схеме при вызове GET /api/users?delay=3')
@pytest.mark.run(order=2)  # определяет порядок выполнения тестов
@pytest.mark.skip("Дубль теста test_check_delayed_response_with_pydantic_schema")  # скипаем тест
def test_check_delayed():
    response = requests.get(url=BASE_URL + BASE_PATH_DELAYED_RESPONSE)
    response_data = Response(response)
    response_data.assert_status_code(200).validate_pydantic_schema(ModelDelayedResponse)


@allure.suite('Методы delayed response')
@allure.title('Код ответа 200 и тело ответа соответствует json схеме при вызове GET /api/users?delay=3')
@pytest.mark.run(order=1)
def test_check_delayed_response_with_pydantic_schema():
    with allure.step("Вызов метода GET /api/users?delay=3"):
        response = requests.get(url=BASE_URL + BASE_PATH_DELAYED_RESPONSE)
    response_data = Response(response)

    with allure.step("Код ответа 200 и тело ответа соответствует json схеме"):
        response_data.assert_status_code(200).validate_pydantic_schema(ModelDelayedResponse)

