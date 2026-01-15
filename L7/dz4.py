import json

filename = "books.json"

with open(filename, "r", encoding="utf-8") as f:
    books = json.load(f)

print(f"Available books:")
for book in books:
    if book["availability"]:
        print(f"- {book['Name']} ({book['Author']}, {book['year']})")

new_book = {"Name": "Python", "Author": "Mark Lutz", "year": 2025, "availability": True}
books.append(new_book)

with open(filename, "w", encoding="utf-8") as f:
    json.dump(books, f, ensure_ascii=False, indent=4)
