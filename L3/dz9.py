"""Порівняння сеттерів/геттерів, декоратора @property та дескрипторів"""


class ProductWithGetSet:
    def __init__(self, name, price):
        self.name = name
        self._price = None
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value


class ProductWithProperty:
    def __init__(self, name, price):
        self.name = name
        self._price = None
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class PriceDescriptor:
    def __init__(self, standart=0.0):
        self._value = standart

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value


class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price


def test_program():
    p1 = ProductWithGetSet("AirPodsPro3", 249)
    print("*** ProductWithGetSet ***")
    print(f"{p1.name} start price: {p1.get_price()}")
    try:
        p1.set_price(279)
        print(f"{p1.name} updated price: {p1.get_price()}")
    except ValueError as e:
        print(f"{p1.name} error: {e}")
    try:
        p1.set_price(-5)
    except ValueError as e:
        print(f"{p1.name} error (negative price): {e}")

    p2 = ProductWithProperty("AirPods4", 139)
    print("\n*** ProductWithProperty ***")
    print(f"{p2.name} start price: {p2.price}")
    try:
        p2.price = 150
        print(f"{p2.name} updated price: {p2.price}")
    except ValueError as e:
        print(f"{p2.name} error: {e}")
    try:
        p2.price = -3
    except ValueError as e:
        print(f"{p2.name} error (negative price): {e}")

    p3 = ProductWithDescriptor("AirPodsPro2", 155)
    print("\n*** ProductWithDescriptor ***")
    print(f"{p3.name} start price: {p3.price}")
    try:
        p3.price = 160
        print(f"{p3.name} updated price: {p3.price}")
    except ValueError as e:
        print(f"{p3.name} error: {e}")
    try:
        p3.price = -1
    except ValueError as e:
        print(f"{p3.name} error (negative price): {e}")


test_program()
