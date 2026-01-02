class MyDescriptorPrice:
    """Дескриптор який керує атрибутом *total* класу Price

    включає також автоматичне округлення
    """

    def __get__(self, instance, owner) -> float:
        return instance._total

    def __set__(self, instance, value) -> None:
        instance._total = round(float(value), 2)


class Price:
    """ Клас для представлення ціни

    який реалізує в методах  арифметичні операції і автоматичне округлення через дескриптор
    """

    total = MyDescriptorPrice()

    def __init__(self, total: float | int) -> None:
        self.total = total

    def __add__(self, other) -> Price:
        return self.total + other.total

    def __sub__(self, other) -> Price:
        return self.total - other.total

    def __eq__(self, other) -> bool:
        return self.total == other.total

    def __lt__(self, other) -> bool:
        return self.total < other.total

    def __repr__(self) -> str:
        return f"Price({self.total})"


p1 = Price(12.32)
p2 = Price(5.567)

print(p1)
print(p2)
print(p2 + p2)
print(p1 - p2)
print(p1 == Price(24))
print(p2 < p1)
print(p1 > p2)
