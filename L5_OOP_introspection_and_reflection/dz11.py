class LimitedAttributesMeta(type):
    """
    Метаклас, який дозволяє класам мати лише фіксовану кількість атрибутів (наприклад, максимум 3).
    Якщо додати більше атрибутів, має виникати помилка
    """
    MAX_ATTRIBUTES: int = 3

    def __new__(mcs, name, bases, attrs):
        user_attrs = [key for key in attrs.keys() if not key.startswith("__")]

        if len(user_attrs) > mcs.MAX_ATTRIBUTES:
            raise TypeError(
                f"Клас {name} не може мати більше {mcs.MAX_ATTRIBUTES} атрибутів."
            )

        return super().__new__(mcs, name, bases, attrs)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    attr4 = 4  # Викличе помилку


obj = LimitedClass()
