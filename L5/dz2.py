def call_function(obj, method_name, *args) -> None:
    """Функція, яка приймає об'єкт, назву методу в вигляді рядка та довільні аргументи для цього методу.
     Функція  викликає відповідний метод об'єкта і повернути результат
     """
    method = getattr(obj, method_name, None)

    if callable(method):
        return method(*args)
    else:
        raise AttributeError(f"Метод '{method_name}' не знайдено або він не викликається.")


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(call_function(calc, "add", 10, 5))
print(call_function(calc, "subtract", 10, 5))
