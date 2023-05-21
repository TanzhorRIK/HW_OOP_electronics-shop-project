import pytest
from src.item import Item, InstantiateCSVError


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


def test_name():
    item = Item('Трубка', 10000, 5)
    item.name = "Phone"
    assert item.name == "Phone"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == item.name


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_instantiate_from_csv_one():
    with pytest.raises(FileNotFoundError) as except_info:
        Item.instantiate_from_csv(path=r"")
    assert 'Отсутствует файл items.csv' in str(except_info.value)

def test_instantiate_from_csv_two():
    with pytest.raises(InstantiateCSVError) as except_info:
        Item.instantiate_from_csv(path=r"../src/items.csv")
    assert 'Файл items.csv поврежден' in str(except_info.value)