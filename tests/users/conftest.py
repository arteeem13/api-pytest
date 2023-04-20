import pytest

"""Условия будут выполняться в тестах в папке tests/users"""


@pytest.fixture()
def condition_users():
    pass  # выполняем перед тестом
    yield  # выполняем тест
    pass  # выполняем после теста


@pytest.fixture(scope="module")
def some():
    pass  # выполняем перед тестами
    yield
    pass  # выполняем после тестов
