"""Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. """


class Animals:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_animals_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' особенности: {self.get_specific()}'


class Fishes(Animals):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animals):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animals):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


class Factory:

    def create_animals(self, kind, name, age, spec):
        if kind.lower() == "fishes":
            return Fishes(kind, name, age, spec)
        elif kind.lower() == "birds":
            return Birds(kind, name, age, spec)
        elif kind.lower() == "mammals":
            return Mammals(kind, name, age, spec)
        else:
            raise ValueError("Данный тип отсутствует.")


factory = Factory()

fishes = factory.create_animals("fishes", "Люся", 7, "крупная")
birds = factory.create_animals("birds", "Гоша", 5, "красный")
mammals = factory.create_animals("mammals", "Боня", 9, "охотничья")

print(fishes.get_animals_info())
print(birds.get_animals_info())
print(mammals.get_animals_info())