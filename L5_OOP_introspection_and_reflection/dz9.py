class DynamicProperties:
    def __init__(self) -> None:
        self._values = {}

    def add_property(self, name: str, value) -> None:
        self._values[name] = value

        def getter(self):
            return self._values[name]

        def setter(self, new_value):
            self._values[name] = new_value

        setattr(self.__class__, name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')

print(obj.name)

obj.name = "Python"
print(obj.name)
