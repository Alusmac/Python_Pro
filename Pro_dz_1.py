"""
ДЗ 1. Introduction. Remind Python basics
) Write a function calculate_circle_area(radius) that:
Takes the radius of a circle.
Returns the area of a circle.
Use this function in a program that asks the user for a radius and prints
out the area.
"""
import math


def calculate_circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is: {area:.2f}")


