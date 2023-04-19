import pytest


@pytest.fixture()
def condition_for_all_tests():
    pass  # выполняем перед тестом
    yield  # выполняем тест
    pass  # выполняем после теста
