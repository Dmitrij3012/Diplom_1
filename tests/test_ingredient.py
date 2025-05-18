class TestIngredient:

    def test_ingredient(self, test_ingredient):

        assert test_ingredient.get_type() == 'sauce'
        assert test_ingredient.get_name() == 'chili'
        assert test_ingredient.get_price() == 200
