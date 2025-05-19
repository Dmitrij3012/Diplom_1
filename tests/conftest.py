from unittest.mock import Mock
import pytest
import data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def test_bun():
    return Bun(data.BUN_NAME, data.BUN_PRICE)


@pytest.fixture
def test_ingredient():
    return Ingredient(data.SAUCE, data.SAUCE_NAME, data.SAUCE_PRICE)


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = data.BUN_NAME
    mock.get_price.return_value = data.BUN_PRICE
    return mock


@pytest.fixture()
def mock_filling():
    mock = Mock()
    mock.get_type.return_value = data.FILLING
    mock.get_name.return_value = data.FILLING_NAME
    mock.get_price.return_value = data.FILLING_PRICE
    return mock


@pytest.fixture()
def mock_sauce():
    mock = Mock()
    mock.get_type.return_value = data.SAUCE
    mock.get_name.return_value = data.SAUCE_NAME
    mock.get_price.return_value = data.SAUCE_PRICE
    return mock


