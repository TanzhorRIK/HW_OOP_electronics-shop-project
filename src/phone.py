from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int,
                 number_of_sim: int):
        self.__number_of_sim = number_of_sim
        super().__init__(name, price, quantity)

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim == 0 and self.__class__.__name__ != int:
            raise ValueError(
                "Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if (self.__class__.__name__ == "Phone" and
                other.__class__.__name__ == "Item" or
                self.__class__.__name__ == other.__class__.__name__ == "Phone"):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только классы Item и Phone")

    def __radd__(self, other):
        if (self.__class__.__name__ == "Phone" and
                other.__class__.__name__ == "Item" or
                self.__class__.__name__ == other.__class__.__name__ == "Phone"):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только классы Item и Phone")
