import pytest


def divide(a: int, b: int) -> float:
    """
    Divides number a by number b.

    >>> divide(6, 2)
    3.0
    >>> divide(5, 0)
    ZeroDivisionError

    """
    if b == 0:
        raise ZeroDivisionError
    return a / b


def test_divide_normal():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    assert divide(-100, 50) == -2.0


def test_divide_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (7, 2, 3.5),
        (-8, 4, -2.0)
    ]
)
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected
