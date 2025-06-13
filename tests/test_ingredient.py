from data import SAUCE, SAUCE_NAME, SAUCE_PRICE


class TestIngredient:

    def test_ingredient_type(self, test_ingredient):

        assert test_ingredient.get_type() == SAUCE

    def test_ingredient_name(self, test_ingredient):

        assert test_ingredient.get_name() == SAUCE_NAME

    def test_ingredient_price(self, test_ingredient):

        assert test_ingredient.get_price() == SAUCE_PRICE
