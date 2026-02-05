class LoggingMeta(type):
    """
    Метаклас, який автоматично додає логування при доступі до будь-якого атрибута класу.
    Кожен раз, коли атрибут змінюється або читається, повинно з'являтися повідомлення в консолі.
    """

    def __new__(mcs, name, bases, attrs):
        original_init = attrs.get("__init__")

        def new_init(self, *args, **kwargs):
            if original_init:
                original_init(self, *args, **kwargs)

            for attr_name in list(self.__dict__.keys()):
                private_name = f"_{attr_name}"
                setattr(self, private_name, getattr(self, attr_name))

                def getter(self, _name=private_name):
                    print(f"Logging: accessed '{_name[1:]}'")
                    return getattr(self, _name)

                def setter(self, value, _name=private_name):
                    print(f"Logging: modified '{_name[1:]}'")
                    setattr(self, _name, value)

                setattr(self.__class__, attr_name, property(getter, setter))

        attrs["__init__"] = new_init
        return super().__new__(mcs, name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'
