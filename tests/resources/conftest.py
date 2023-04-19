import pytest


@pytest.fixture()
def condition_resources():
    pass  # выполняем перед тестом
    yield  # выполняем тест
    pass  # выполняем после теста
