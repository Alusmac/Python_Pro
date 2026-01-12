class ReverseFileIteratorSimple:
    """власний ітератор, який буде зчитувати файл у зворотному

    порядку — рядок за рядком з кінця файлу до початку
    """

    def __init__(self, filename:str) -> None:
        self.lines = open(filename, "r", encoding="utf-8").read().splitlines()

    def __iter__(self):
        for line in reversed(self.lines):
            yield line


reading = ReverseFileIteratorSimple("test1.txt")

for line in reading:
    print(line)
