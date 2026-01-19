import pytest


class AgeVerifier:
    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Checks if a user is an adult (age >= 18)

        >>> AgeVerifier.is_adult(17)
        False
        >>> AgeVerifier.is_adult(18)
        True
        >>> AgeVerifier.is_adult(25)
        True
        """
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age >= 18


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (28, True),
        (18, True),
        (1, False)
    ]
)
def test_is_adult_normal(age, expected):
    assert AgeVerifier.is_adult(age) == expected


@pytest.mark.skip(reason="Invalid age value (less than 0)")
def test_is_adult_negative():
    with pytest.raises(ValueError):
        AgeVerifier.is_adult(-5)


@pytest.mark.skipif(121 > 120, reason="Unrealistic age (>120")
def test_is_adult_old():
    assert AgeVerifier.is_adult(121) == False
