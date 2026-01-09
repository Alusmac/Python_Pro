def analyze_inheritance(cls: type) -> type:
    """
    Аналізує успадкування класу і виводить методи, які він отримав від батьків
    """
    print(f"Клас {cls.__name__} наслідує:")

    own_methods = set(cls.__dict__.keys())

    inherited_methods = []

    for base in cls.__bases__:
        for attr_name, attr_value in base.__dict__.items():
            if callable(attr_value) and attr_name not in own_methods and not attr_name.startswith("__"):
                inherited_methods.append((attr_name, base.__name__))

    if inherited_methods:
        for name, base_name in inherited_methods:
            print(f"- {name} з {base_name}")
    else:
        print("- <немає успадкованих методів>")


class Parent:
    def parent_method(self) -> None:
        pass


class Child(Parent):
    def child_method(self) -> None:
        pass


analyze_inheritance(Child)
