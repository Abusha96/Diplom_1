from unittest.mock import Mock

from praktikum.burger import Burger
from tests.data import EXPECTED_RECEIPT


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients == [ingredient_mock]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert not burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100.0
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 150.0
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 350.0

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Parmesan Bun"
        bun_mock.get_price.return_value = 100.0

        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Tuna"
        ingredient_mock.get_type.return_value = "FILLING"
        ingredient_mock.get_price.return_value = 150.0

        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        actual_receipt = burger.get_receipt().strip()

        assert EXPECTED_RECEIPT == actual_receipt
