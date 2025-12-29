class Rectangle:
    """
    Class representing a rectangle.
    """

    def __init__(self, rect_width: float, rect_height: float) -> None:
        """
        Initialize a rectangle object.

        :param rect_width: Width of the rectangle
        :param rect_height: Height of the rectangle
        """
        self.width = rect_width
        self.height = rect_height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Check whether the rectangle is a square.
        """
        return self.width == self.height

    def resize(self, new_rect_width: float, new_rect_height: float) -> None:
        """
        Resize the rectangle.

        :param new_rect_width: New width
        :param new_rect_height: New height
        """
        self.width = new_rect_width
        self.height = new_rect_height


rectangle = Rectangle(5, 15)

print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
print("Is square?:", rectangle.is_square())

print("Resizing rectangle...")
rectangle.resize(20, 20)

print("New width:", rectangle.width)
print("New height:", rectangle.height)
print("New area:", rectangle.area())
print("New perimeter:", rectangle.perimeter())
print("Is square?:", rectangle.is_square())
