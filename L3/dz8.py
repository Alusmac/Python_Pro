class MyDescriptorPrice:
    def __get__(self, instance, owner):
        return instance._total

    def __set__(self, instance, value):
        instance._total = round(float(value), 2)


class Price:
    total = MyDescriptorPrice()

    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __eq__(self, other):
        return self.total == other.total

    def __lt__(self, other):
        return self.total < other.total

    def __repr__(self):
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
