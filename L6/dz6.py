class FileIterator:
    """тератор, який буде повертати всі файли в заданому каталозі по черзі.
    Для кожного файлу виведіть його назву та розмір
    """

    def __init__(self, files) -> None:
        self.files = files
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        file_name = self.files[self.index]
        try:
            f = open(file_name, 'rb')
            f.seek(0, 2)
            size = f.tell()
            f.close()
        except FileNotFoundError:
            size = 0
        self.index += 1
        return file_name, size


files = ["test1.txt", "test4.txt", "test5.txt"]
for name, size in FileIterator(files):
    print(f"Файл: {name}, Розмір: {size} байт")
