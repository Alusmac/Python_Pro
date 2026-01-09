class TypeCheckedMeta(type):
    """ метаклас TypeCheckedMeta, який перевіряє типи атрибутів при їх встановленні.
     Якщо тип значення не відповідає типовому опису, має виникати помилка
     """

    def __new__(cls, name, bases, namespace):
        expected_types = {'name': str, 'age': int}

        def __setattr__(self, key, value):
            if key in expected_types and not isinstance(value, expected_types[key]):
                raise TypeError(
                    f"Для атрибута '{key}' очікується тип '{expected_types[key].__name__}', "
                    f"але отримано '{type(value).__name__}'"
                )
            object.__setattr__(self, key, value)

        namespace['__setattr__'] = __setattr__
        return super().__new__(cls, name, bases, namespace)


class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # все добре
p.age = "30"  ## Викличе помилку, очікується int
