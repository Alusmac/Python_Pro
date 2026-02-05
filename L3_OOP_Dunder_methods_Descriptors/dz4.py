"""Реалізуйте клас BinaryNumber, який представляє двійкове число"""


class BinaryNumber:
    """клас BinaryNumber, який представляє двійкове число

    який включає методи для виконання двійкових операцій
    """

    def __init__(self, binary: str) -> None:
        self.binary = binary
        self.number = int(binary, 2)

    def __and__(self, other):
        return BinaryNumber(bin(self.number & other.number)[2:])

    def __or__(self, other):
        return BinaryNumber(bin(self.number | other.number)[2:])

    def __xor__(self, other):
        return BinaryNumber(bin(self.number ^ other.number)[2:])

    def __invert__(self):
        how_many = (1 << len(self.binary)) - 1
        return BinaryNumber(bin((~self.number) & how_many)[2:])

    def __str__(self) -> str:
        return self.binary


b1 = BinaryNumber("10110")
b2 = BinaryNumber("11010")

print(b1)
print(b2)
print(b1 == b2)
print(b1 & b2)
print(b1 | b2)
print(b1 ^ b2)
