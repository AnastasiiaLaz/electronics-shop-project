from src import item


class MixinLang:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self.__language

    @property
    def language(self):
        return self.__language


class Keyboard(item.Item, MixinLang):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
