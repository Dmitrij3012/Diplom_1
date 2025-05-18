class TestBun:

    def test_bun(self, test_bun):

        assert test_bun.get_name() == 'white bun'
        assert test_bun.get_price() == 300
