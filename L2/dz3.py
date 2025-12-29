"""Магазин замовлень з акційними знижками"""
discount = 0.1


def create_order(price: int | float) -> None:
    """ Функція яка робить звичайну знижку 10 відсотків

    """
    price_with_discount = price * (1 - discount)
    print(f"Початкова ціна: {price}, Ціна зі знижкою 10%: {price_with_discount}")

    def apply_additional_discount(vip_discount: int | float) -> None:
        nonlocal price
        price *= (1 - vip_discount)
        print(f"Додаткова для VIP покупця знижка: {vip_discount}, Ціна до оплати: {price}")

    apply_additional_discount(0.2)


create_order(1000)  # Початкова ціна: 1000, кінцева ціна зі знижкою 10%: 900
