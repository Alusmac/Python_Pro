"""
ДЗ 1. Introduction. Remind Python basics
) Write a function calculate_circle_area(radius) that:
Takes the radius of a circle.
Returns the area of a circle.
Use this function in a program that asks the user for a radius and prints out the area.
2) Create a Rectangle class that represents a rectangle.
Class requirements:
Class attributes:
width — the width of the rectangle.
height — the height of the rectangle.
Class methods:
__init__(self, width, height) — a constructor that accepts the width and height of the rectangle.
area(self) — a method that returns the area of the rectangle.
perimeter(self) — a method that returns the perimeter of the rectangle.
is_square(self) — a method that returns True if the rectangle is a square (the width is equal to the height), otherwise False.
resize(self, new_width, new_height) — a method that changes the width and height of the rectangle.
Create an object of the Rectangle class and test all the methods.
"""
import math


def calculate_circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is: {area:.2f}")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

rectangle = Rectangle(5, 15)

print("*" * 30)
print("Width of the rectangle:", rectangle.width)
print("Height of the rectangle:", rectangle.height)
print("Area of the rectangle:", rectangle.area())
print("Perimeter of the rectangle:", rectangle.perimeter())
print("Square is? :", rectangle.is_square())

print("Changing size of Object:")
rectangle.resize(20, 20)

print("New width:", rectangle.width)
print("New height:", rectangle.height)
print("New Area:", rectangle.area())
print("New Perimeter:", rectangle.perimeter())
print("Square is?:", rectangle.is_square())


