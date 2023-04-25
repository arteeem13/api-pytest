import allure
import pytest
import requests

from src.base_classes.pydantic_schema_validate_response import Response
from src.configurations.constants import BASE_URL
from src.schemas.pydantic_schemas.create_user import ModelCreateUser


@allure.suite('Методы users')
@pytest.mark.users_test
@pytest.mark.parametrize('users_name, users_job', [
    ('morpheus', 'leader'),
    ('Artem', 'QA-engineer'),
    ('Эмма Уотсон', 'Актриса 2023'),
])
@allure.title('Создание юзера c {users_name} и {users_job}')
def test_create_user(users_name, users_job):
    """Создание юзера с разными входными данными"""
    request_body = {
        'name': users_name,
        'job': users_job
    }
    with allure.step("Вызов метода POST /api/users"):
        response = requests.post(url=BASE_URL + "api/users,", data=request_body)
    response_data = Response(response)

    with allure.step("Код ответа 201 и тело ответа соответствует json схеме"):
        response_data.assert_status_code(201).validate_pydantic_schema(ModelCreateUser)
