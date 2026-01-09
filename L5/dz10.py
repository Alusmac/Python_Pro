class SingletonMeta(type):
    """
    Метаклас SingletonMeta, який гарантує, що клас може мати лише один екземпляр (патерн Singleton)
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self) -> None:
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()

print(obj1 is obj2)  # True
