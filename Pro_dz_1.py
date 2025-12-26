import math


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle by its radius.

    :param radius: Radius of the circle
    :return: Area of the circle
    """
    return math.pi * radius**2


radius: float = float(input("Enter the radius of the circle: "))
area: float = calculate_circle_area(radius)

print(f"The area of the circle is: {area:.2f}")



