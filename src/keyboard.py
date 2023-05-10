from src.item import Item


class MixLanguage:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        elif self.language == 'RU':
            self.__language = 'EN'
        return self

class Keyboard(Item, MixLanguage):
    def __int__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name