from unittest.mock import Mock
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def test_bun():
    return Bun('white bun', 300)


@pytest.fixture
def test_ingredient():
    return Ingredient('sauce', 'chili', 200)


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = 'white bun'
    mock.get_price.return_value = 200
    return mock


@pytest.fixture()
def mock_filling():
    mock = Mock()
    mock.get_type.return_value = 'filling'
    mock.get_name.return_value = 'cutlet'
    mock.get_price.return_value = 300
    return mock


@pytest.fixture()
def mock_sauce():
    mock = Mock()
    mock.get_type.return_value = 'sauce'
    mock.get_name.return_value = 'chili'
    mock.get_price.return_value = 200
    return mock

