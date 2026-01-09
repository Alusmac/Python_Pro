class Proxy:
    def __init__(self, obj) -> None:
        self._obj = obj

    def __getattr__(self, name: str) -> object:
        """
        Викликається, коли звертаються до атрибута, якого немає в Proxy
        """
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs):
                print("Calling method:")
                print(f"{name} with args: {args}")
                return attr(*args, **kwargs)

            return wrapper
        else:
            return attr


class MyClass:
    def greet(self, name: str) -> object:
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

result = proxy.greet("Alice")
print(result)
