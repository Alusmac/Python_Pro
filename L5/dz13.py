class AutoMethodMeta(type):
    """метаклас AutoMethodMeta, який автоматично генерує методи геттера та сеттера для кожного атрибута класу
    """

    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in list(dct.items()):

            if attr_name.startswith("__") and attr_name.endswith("__"):
                continue

            def make_getter(attr):
                def getter(self):
                    return getattr(self, attr)

                return getter

            def make_setter(attr):
                def setter(self, value):
                    setattr(self, attr, value)

                return setter

            dct[f"get_{attr_name}"] = make_getter(attr_name)
            dct[f"set_{attr_name}"] = make_setter(attr_name)

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
