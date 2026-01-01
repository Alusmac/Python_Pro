"""to-Compare"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"


students = [
    Person("Samuel", 23),
    Person("Tifanny", 45),
    Person("Robert", 18),
    Person("Emma", 26), ]

print(sorted(students))
