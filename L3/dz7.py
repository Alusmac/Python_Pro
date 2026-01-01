import math


class Vector:
    """клас Vector, який представляє вектор у просторі з n вимірами"""

    def __init__(self, detals):
        self.detals = detals

    def __add__(self, other):
        return Vector(list(map(lambda a, b: a + b, self.detals, other.detals)))

    def __sub__(self, other):
        return Vector(list(map(lambda a, b: a - b, self.detals, other.detals)))

    def __mul__(self, other):
        return Vector(sum(map(lambda a, b: a * b, self.detals, other.detals)))

    def size_len(self):
        return math.sqrt(sum(map(lambda x: x * x, self.detals)))

    def __eq__(self, other):
        return self.size_len() == other.size_len()

    def __lt__(self, other):
        return self.size_len() < other.size_len()

    def __repr__(self):
        return f"Vector({self.detals})"


v1 = Vector([3, 2, 1])
v2 = Vector([4, 5, 4])

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 < v2)
