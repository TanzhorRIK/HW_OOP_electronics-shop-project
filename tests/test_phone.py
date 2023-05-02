import pytest
from src.phone import Phone, Item


@pytest.fixture
def items():
    return (
        Phone("iPhone 14", 120_000, 5, 2), Phone("iPhone 14", 140_000, 5, 1),
        Item("Смартфон", 10000, 20), 2)


def test_repr(items):
    assert repr(items[0]) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(items):
    for i in range(len(items) - 1):
        if (items[i].__class__.__name__ == "Phone" and
                items[i + 1].__class__.__name__ == "Item" or
                items[i].__class__.__name__ == items[
                    i + 1].__class__.__name__ == "Phone"):
            assert items[0] + items[1] == 10
        else:
            with pytest.raises(TypeError):
                items[i] + items[i + 1]


def test_add(items):
    for i in range(len(items) - 1):
        if (items[i].__class__.__name__ == "Phone" and
                items[i + 1].__class__.__name__ == "Item" or
                items[i].__class__.__name__ == items[
                    i + 1].__class__.__name__ == "Phone"):
            assert items[0] + items[1] == 10
        else:
            with pytest.raises(TypeError):
                items[i] + items[i + 1]


def test_radd(items):
    for i in range(1, len(items) - 1):
        if (items[i - 1].__class__.__name__ == "Phone" and
                items[i].__class__.__name__ == "Item" or
                items[i].__class__.__name__ == items[
                    i - 1].__class__.__name__ == "Phone"):
            assert items[1] + items[2] == 25
        else:
            with pytest.raises(TypeError) as excinfo:
                items[i] + items[i + 1]
            assert "Складывать можно только классы Item и Phone" in str(
                excinfo.value)


def test_number_of_sim(items):
    item = items[1]
    with pytest.raises(ValueError) as excinfo:
        item.number_of_sim = 0

    assert "Количество физических SIM-карт должно быть целым числом больше нуля." in str(
        excinfo.value)
