import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', [
        ['кабачковая икра', 15000],
        ['ультрамарин', 600],
        ['экзистенциальный кризис', 0]
    ])
    def test_get_name(self, name, price):
        bun_1 = Bun(name, price)
        assert bun_1.get_name() == name

    @pytest.mark.parametrize('name, price', [
        ['кабачковая икра', 15000],
        ['ультрамарин', 600],
        ['экзистенциальный кризис', 0]
    ])
    def test_get_price(self, name, price):
        bun_1 = Bun(name, price)
        assert bun_1.get_price() == price
