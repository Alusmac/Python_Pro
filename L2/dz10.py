"""Створення товарів для онлайн-магазину"""


def create_product(name: str) -> str:
   def next_price(price:int|float) -> int|float:
       def next_several(several:int) -> int:
           return {"Назва": name, "ціна": price, "кількіть": several}
       return next_several
   return next_price


product_creator = create_product("Ноутбук")
product_with_price = product_creator(31000)
product = product_with_price(5)
print(product)

def change_price_produkt(produkt:dict) -> dict:
    def change_price(new_price:int) -> int|float:
        product["price"] = new_price
        print(f"Для цього Товару {product['Назва']} нова ціна {new_price}")
    return change_price


change_price = change_price_produkt(product)
change_price(34500)
print(product)
