import pytest
from src.item import Item


@pytest.fixture
def items():
    return Item("Смартфон", 10000, 20), Item("Ноутбук", 20000, 5)

def test_calculate_total_price(items):
        assert items[0].calculate_total_price() == 200000
        assert items[1].calculate_total_price() == 100000


def test_apply_discount(items):
    items[0].pay_rate = 0.8
    for item in items:
        item.apply_discount()
    assert items[0].price == 8000.0
    assert items[1].price == 20000
