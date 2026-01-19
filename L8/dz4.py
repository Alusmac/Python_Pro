import doctest


def is_even(n: int) -> bool:
    """
    Checks whether a number is even.

    >>> is_even(2)
    True
    >>> is_even(3)
    False

    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calculates the factorial of a number (n)

    >>> factorial(5)
    120
    >>> factorial(3)
    6
    """
    if n < 0:
        raise ValueError
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    doctest.testmod()
