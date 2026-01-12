def increment_average(file_path:str, step=10) -> None:
    """генератор, який по черзі зчитує великий файл даних
     (наприклад, числові показники продуктивності), обчислює середнє значення
      на кожній ітерації та оновлює результат. Це корисно для обробки великих даних,
      які не можна завантажити повністю в пам'ять.
    """
    total = 0.0
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                num = float(line)
            except ValueError:
                continue
            count += 1
            total += num
            if count % step == 0:
                yield total / count
        if count % step != 0:
            yield total / count


for avg in increment_average("test11.txt"):
    print(f"Поточне середнє: {avg:.2f}")
