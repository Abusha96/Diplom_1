import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('type, name, price', [
        [INGREDIENT_TYPE_SAUCE, 'кабачковая икра', 15000],
        [INGREDIENT_TYPE_FILLING, 'ультрамарин', 600],
        [INGREDIENT_TYPE_FILLING, 'экзистенциальный кризис', 0]
        ])
    def test_get_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('type, name, price', [
        [INGREDIENT_TYPE_SAUCE, 'кабачковая икра', 15000],
        [INGREDIENT_TYPE_FILLING, 'ультрамарин', 600],
        [INGREDIENT_TYPE_FILLING, 'экзистенциальный кризис', 0]
    ])
    def test_get_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type, name, price', [
        [INGREDIENT_TYPE_SAUCE, 'кабачковая икра', 15000],
        [INGREDIENT_TYPE_FILLING, 'ультрамарин', 600],
        [INGREDIENT_TYPE_FILLING, 'экзистенциальный кризис', 0]
    ])
    def test_get_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type
