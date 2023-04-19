import pytest


@pytest.fixture()
def condition_users():
    pass  # выполняем перед тестом
    yield  # выполняем тест
    pass  # выполняем после теста
