import allure
import pytest
import requests

from src.base_classes.jsonschema_validate_response import Response
from src.configurations.constants import BASE_URL, BASE_PATH_SINGLE_USER
from src.schemas.json_schemas.get_single_user import SINGLE_USER_SCHEMA


@allure.suite('Методы users')
@pytest.mark.users_test
@pytest.mark.parametrize('user_id, first_name, last_name', [
    (1, 'George', 'Bluth'),
    (2, 'Janet', 'Weaver'),
    (3, 'Emma', 'Wong'),
    (4, 'Eve', 'Holt'),
    (5, 'Charles', 'Morris'),
    (6, 'Tracey', 'Ramos')
])
@allure.title('Код ответа 200 и тело ответа соответствует json схеме при вызове GET /api/unknown/{user_id}')
def test_check_response_with_jsonschema(user_id, first_name, last_name):
    """Получение данных пользователя с id = user_id"""
    with allure.step("Вызов метода GET /api/unknown/{0}".format(user_id)):
        response = requests.get(url=BASE_URL + BASE_PATH_SINGLE_USER + str(user_id))
    response_data = Response(response)
    with allure.step("Код ответа 200 и тело ответа соответствует json схеме"):
        response_data.assert_status_code(200).validate_json_schema(SINGLE_USER_SCHEMA)

    response_body = response.json()
    users_email = "{0}.{1}@reqres.in".format(first_name, last_name).lower()

    with allure.step("id в теле ответа = {0}".format(user_id)):
        assert response_body.get("data").get("id") == user_id

    with allure.step("first_name в теле ответа = {0}".format(first_name)):
        assert response_body.get("data").get("first_name") == first_name

    with allure.step("last_name в теле ответа = {0}".format(last_name)):
        assert response_body.get("data").get("last_name") == last_name

    with allure.step("email в теле ответа = {0}".format(users_email)):
        assert response_body.get("data").get("email") == users_email

    # assert response_body.get("data").get("email") == users_email
