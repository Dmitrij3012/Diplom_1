from praktikum.database import Database


class TestDatabase:

    def test_available_bun(self):
        database = Database()

        assert database.buns == database.available_buns()
        assert len(database.buns) == 3

        assert database.ingredients == database.available_ingredients()
        assert len(database.ingredients) == 6
