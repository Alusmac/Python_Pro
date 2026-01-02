"""to-Compare"""


class Person:
    """"клас Person із параметрами name та age

    включає в себе методи для порівняння за віком
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __lt__(self, other) -> bool:
        return self.age < other.age

    def __eq__(self, other) -> bool:
        return self.age == other.age

    def __gt__(self, other) -> bool:
        return self.age > other.age

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


students = [
    Person("Samuel", 23),
    Person("Tifanny", 45),
    Person("Robert", 18),
    Person("Emma", 26), ]

print(sorted(students))
