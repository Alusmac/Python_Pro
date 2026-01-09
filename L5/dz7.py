def log_methods(cls: type) -> None:
    """
    Декоратор класу, який логуватиме виклики всіх його методів
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            def wrapper(self, *args, _method=attr_value, _name=attr_name, **kwargs):
                print(f"Logging: {_name} called with {args}")
                return _method(self, *args, **kwargs)

            setattr(cls, attr_name, wrapper)
    return cls


@log_methods
class MyClass:
    def add(self, a, b) -> None:
        return a + b

    def subtract(self, a, b) -> None:
        return a - b


obj = MyClass()
obj.add(5, 3)
obj.subtract(5, 3)
