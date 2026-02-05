"""Dunder methods"""


class Fraction:
    """клас  (дробові числа).

     який має методи для додавання, віднімання,
     множення та ділення двох об'єктів цього класу
     """

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(self.numerator + other.numerator, self.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator - other.numerator, self.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator / other.numerator, self.denominator)

    def __repr__(self) -> str:
        return f"Fraction {self.numerator}/{self.denominator} "


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
