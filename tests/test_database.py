import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize('name, price', [
        ['black bun', 100],
        ['white bun', 200],
        ['red bun', 300]
    ])
    def test_available_buns(self, name, price):
        database = Database()
        available_bun = None
        for bun in database.available_buns():
            if name == bun.name and price == bun.price:
                available_bun = bun
        assert available_bun

    @pytest.mark.parametrize("ingredient_type, name, price", [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [INGREDIENT_TYPE_FILLING, "sausage", 300]
    ])
    def test_available_ingredients(self, ingredient_type, name, price):
        database = Database()
        available_ingredient = None
        for ingredient in database.available_ingredients():
            if ingredient_type == ingredient.type and name == ingredient.name and price == ingredient.price:
                available_ingredient = ingredient
        assert available_ingredient
