class BinaryIterator:
    """ ітератор який використовує менеджер контексту для зчитування бінарних файлів великими
    блоками даних (наприклад, по 1024 байти). Виведіть кількість прочитаних байт.
    """

    def __init__(self, file_path: str, read_size: int = 1024) -> None:
        self.file = open(file_path, 'rb')
        self.read_size = read_size

    def __iter__(self):
        return self

    def __next__(self):
        read = self.file.read(self.read_size)
        if not read:
            self.file.close()
            raise StopIteration
        return read


total = 0
for block in BinaryIterator("test12.bin"):
    total += len(block)

print(f"Прочитано {total} байт")
