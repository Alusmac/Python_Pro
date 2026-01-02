"""Numeric-like"""
import math


class Vector:
    """клас Vector, що підтримує операції додавання,

     віднімання, множення на число та порівняння за довжиною
     """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __lt__(self, other) -> bool:
        return self.length() < other.length()

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)
print(v1 - v2)
print(v2 * v1)
print(v1.length())
print(v1 == v2)
