def analyze_object(obj) -> None:
    """функція яка виводить тип об'єкта
    """

    print(f"Тип об'єкта: {type(obj)}")
    print("Атрибути і методи:")

    attributes = dir(obj)

    for attr in attributes:
        if attr.startswith("__") and attr.endswith("__"):
            continue

        value = getattr(obj, attr)
        print(f"- {attr}: {type(value)}")


class MyClass:
    def __init__(self, value) -> None:
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
