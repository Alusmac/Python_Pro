def limited_even_numbers(limit:int) -> None:
    """генератор, який генерує нескінченну послідовність парних чисел
    """
    n = 0
    for _ in range(limit):
        yield n
        n += 2


with open("test5.txt", "w") as f:
    for num in limited_even_numbers(100):
        f.write(f"{num}\n")

print("100 парних чисел збережено у test5.txt")
