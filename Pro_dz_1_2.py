class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance.

        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        :return: Area of the rectangle
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        :return: Perimeter of the rectangle
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Check whether the rectangle is a square.

        :return: True if width equals height, otherwise False
        """
        return self.width == self.height

    def resize(self, new_width: float, new_height: float) -> None:
        """
        Resize the rectangle.

        :param new_width: New width of the rectangle
        :param new_height: New height of the rectangle
        """
        self.width = new_width
        self.height = new_height


rectangle: Rectangle = Rectangle(5, 15)

print("Width of the rectangle:", rectangle.width)
print("Height of the rectangle:", rectangle.height)
print("Area of the rectangle:", rectangle.area())
print("Perimeter of the rectangle:", rectangle.perimeter())
print("Square is?:", rectangle.is_square())

print("Changing size of object:")
rectangle.resize(20, 20)

print("New width:", rectangle.width)
print("New height:", rectangle.height)
print("New area:", rectangle.area())
print("New perimeter:", rectangle.perimeter())
print("Square is?:", rectangle.is_square())
