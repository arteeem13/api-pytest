import string

import pytest
import requests

from configurations.constants import BASE_URL, BASE_PATH_SINGLE_USER
from src.base_classes.jsonschema_validate_response import Response
from src.schemas.json_schemas.get_single_user import SINGLE_USER_SCHEMA


@pytest.mark.parametrize('user_id, first_name, last_name', [
    (1, 'George', 'Bluth'),
    (2, 'Janet', 'Weaver'),
    (3, 'Emma', 'Wong'),
    (4, 'Eve', 'Holt'),
    (5, 'Charles', 'Morris'),
    (6, 'Tracey', 'Ramos')
])
def test_check_response_with_jsonschema(user_id, first_name, last_name):
    response = requests.get(url=BASE_URL + BASE_PATH_SINGLE_USER + str(user_id))
    response_data = Response(response)
    response_data.assert_status_code(200).validate_json_schema(SINGLE_USER_SCHEMA)

    response_body = response.json()
    assert response_body.get("data").get("id") == user_id
    assert response_body.get("data").get("first_name") == first_name
    assert response_body.get("data").get("last_name") == last_name
    assert response_body.get("data").get("email") == "{0}.{1}@reqres.in".format(first_name, last_name).lower()
    # assert response_body.get("data").get("email") == ("%s.%s@reqres.in" % (first_name, last_name)).lower()
