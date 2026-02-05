import importlib
import inspect


def analyze_module(module_name) -> None:
    """ Функція, яка приймає на вхід назву модуля (рядок) та виводить список усіх класів,
     функцій та їхніх сигнатур у модулі
     """
    module = importlib.import_module(module_name)

    print("Функції:")
    funcs = []

    for name, obj in inspect.getmembers(module):
        if inspect.isbuiltin(obj) or inspect.isfunction(obj):
            try:
                sig = str(inspect.signature(obj))
                sig = sig.replace(", /", "").replace(" /", "")
                funcs.append(f"- {name}{sig}")
            except (ValueError, TypeError):
                funcs.append(f"- {name}()")

    if funcs:
        print("\n".join(funcs))
    else:
        print("- <немає функцій у модулі>")

    print("\nКласи:")
    classes = []

    for name, obj in inspect.getmembers(module, inspect.isclass):
        classes.append(f"- {name}")

    if classes:
        print("\n".join(classes))
    else:
        print("- <немає класів у модулі math>")


print(analyze_module("math"))
