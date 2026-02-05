""" Mоя домашня бібліотека книжок; рахую сторінки в книжках"""


class MyBooksCollection:
    """ клас моєї бібдіотеки,

    який реальзіє методи рахування книжок, сторінок і шукати найменшу книгу за кількістю сторінок
    """

    def __init__(self, books) -> None:
        self.books = books

    def __len__(self) -> int:
        return sum(1 for book in self.books)

    def __iter__(self):
        return iter(self.books)

    def total_pages(self) -> int:
        return sum(self.books)

    def min_pages(self) -> int:
        return min(self.books)


books = MyBooksCollection([30, 49, 543, 340, 65])

print("How many books I have:", len(books))
print("How many pages total in this books I have:", books.total_pages())
print("Min pages in one of the most small books I have:", books.min_pages())
