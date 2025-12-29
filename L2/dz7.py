""" Трекер витрат """
total_expense = 0


def add_expense(expense: int | float) -> None:
    """ функція, яка приймає суму витрат і додає її до загальної суми
    """
    global total_expense
    total_expense += expense


def get_expense() -> float:
    """ функція, яка повертає загальну суму витрат
    """
    return total_expense


print("Вас вітає Трекер витрат, який порахує скільки ви витратили.")
print("Введіть суму яку ви витратили, або '=' щоб побачити всього скільки витрат, 'end' щоб вийти.")

while True:
    user = input("Введіть суму або '=': ")
    if user == "end":
        break
    if user == "=":
        print(f"Всього витрачено: {get_expense()}")
    else:
        try:
            expense = float(user)
            add_expense(expense)
            print(f"Додано до витрат: {expense}")
        except ValueError:
            print("Введіть команду 'end' або '='")
