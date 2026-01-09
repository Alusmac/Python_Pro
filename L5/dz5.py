class MutableClass:
    """клас MutableClass, який має методи для динамічного додавання та видалення атрибутів об'єкта
    """

    def add_attribute(self, name: str, value) -> None:
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        if hasattr(self, name):
            delattr(self, name)
        else:
            print(f"Атрибут '{name}' не існує.")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")

# print(obj.name)   # Виникне помилка, атрибут видалений
