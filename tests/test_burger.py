from unittest.mock import Mock
import pytest
import data
from praktikum.burger import Burger


class TestBurger:

    def test_burger_bun(self, mock_bun):

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
        assert burger.bun.get_name() == data.BUN_NAME
        assert burger.bun.get_price() == data.BUN_PRICE
        assert burger.get_price() == data.BUN_PRICE_IN_BURGER

    def test_burger_ingredient(self, mock_filling):

        burger = Burger()
        burger.add_ingredient(mock_filling)

        assert burger.ingredients == [mock_filling]
        assert burger.ingredients[0].get_type() == data.FILLING
        assert burger.ingredients[0].get_name() == data.FILLING_NAME
        assert burger.ingredients[0].get_price() == data.FILLING_PRICE

    def test_burger_remove_ingredient(self, mock_sauce):

        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)

        assert burger.ingredients == []
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredients(self, mock_filling, mock_sauce):

        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0].get_type() == data.FILLING
        assert burger.ingredients[0].get_name() == data.FILLING_NAME
        assert burger.ingredients[0].get_price() == data.FILLING_PRICE
        assert burger.ingredients[1].get_type() == data.SAUCE
        assert burger.ingredients[1].get_name() == data.SAUCE_NAME
        assert burger.ingredients[1].get_price() == data.SAUCE_PRICE

    @pytest.mark.parametrize(
        'bun_name, bun_price, filling_type, filling_name, filling_price,'
        'sauce_type, sauce_name, sauce_price, burger_price', data.PARAMETRIZE_DATA)
    def test_price(
            self, bun_name, bun_price, filling_type, filling_name, filling_price,
            sauce_type, sauce_name, sauce_price, burger_price):
        bun = Mock()
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = bun_price

        filling = Mock()
        filling.get_type.return_value = filling_type
        filling.get_name.return_value = filling_name
        filling.get_price.return_value = filling_price

        sauce = Mock()
        sauce.get_type.return_value = sauce_type
        sauce.get_name.return_value = sauce_name
        sauce.get_price.return_value = sauce_price

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(filling)
        burger.add_ingredient(sauce)

        assert burger.get_price() == burger_price

    def test_receipt(self, mock_bun, mock_filling, mock_sauce):

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)

        assert burger.get_receipt() == data.RECEIPT_DATA
