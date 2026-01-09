class MutableClass:
    def add_attribute(self, name: str, value) -> None:
        """
        Додає атрибут з ім'ям name та значенням value
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """
        Видаляє атрибут з ім'ям name
        """
        if hasattr(self, name):
            delattr(self, name)
        else:
            print(f"Атрибут '{name}' не існує.")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)

obj.remove_attribute("name")

# print(obj.name)  # розкоментування викличе помилку
