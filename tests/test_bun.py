from data import BUN_NAME, BUN_PRICE


class TestBun:

    def test_bun_name(self, test_bun):

        assert test_bun.get_name() == BUN_NAME

    def test_bun_price(self, test_bun):

        assert test_bun.get_price() == BUN_PRICE
