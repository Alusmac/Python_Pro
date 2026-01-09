def create_class(class_name: str, methods) -> None:
    """ Функція, яка створює клас з заданим іменем та методами.
    """
    return type(class_name, (object,), methods)


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())
print(obj.say_goodbye())
