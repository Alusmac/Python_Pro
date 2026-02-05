"""Менеджер підписки на розсилку"""
subscribers = []


def subscribe(name: str) -> str:
    """Функція яка приймає ім'я підписника як аргумент
    і додає його до списку підписників
    """
    subscribers.append(name)

    def confirm_subscription():
        return f"Підписка підтверджена для: {name}"

    return confirm_subscription()


def unsubscribe(name: str) -> str:
    """яка приймає ім'я та видаляє його зі списку підписників
    """
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} успішно відписаний"

    return f"{name} такого імені немає"


subscribe("Олена")
subscribe("Ігор")
print(subscribers)  # ['Олена', 'Ігор']
print(unsubscribe("Ігор"))  # 'Ігор успішно відписаний'
print(subscribers)  # ['Олена']
