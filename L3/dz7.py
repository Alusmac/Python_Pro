import math


class Vector:
    """клас Vector, який представляє вектор у просторі з n вимірами

    який включає методи для додавання, віднімання векторів та обчислення скалярного добутку
    """

    def __init__(self, detals:float) -> None:
        self.detals = detals

    def __add__(self, other) -> "Vector":
        return Vector(list(map(lambda a, b: a + b, self.detals, other.detals)))

    def __sub__(self, other) -> "Vector":
        return Vector(list(map(lambda a, b: a - b, self.detals, other.detals)))

    def __mul__(self, other) -> "Vector":
        return Vector(sum(map(lambda a, b: a * b, self.detals, other.detals)))

    def size_len(self) -> float :
        return math.sqrt(sum(map(lambda x: x * x, self.detals)))

    def __eq__(self, other) -> bool:
        return self.size_len() == other.size_len()

    def __lt__(self, other) -> bool:
        return self.size_len() < other.size_len()

    def __repr__(self) -> str:
        return f"Vector({self.detals})"


v1 = Vector([3, 2, 1])
v2 = Vector([4, 5, 4])

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 < v2)
