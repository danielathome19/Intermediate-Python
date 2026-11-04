# cd lecture17
import csv
from flask import Flask


app = Flask(__name__)

def load_books() -> list[dict]:
    with open("books.csv", mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def find_book(books: list[dict], title: str):
    return next((b for b in books if b["Title"].lower() == title.lower()), None)

@app.get('/books/<title>')
def get_book(title: str):
    books = load_books()
    book = find_book(books, title)
    if not book:
        return {'error': 'Book not found'}, 404
    return book


if __name__ == "__main__":
    print("Run with: flask --app flask_books run")  # cd lecture17
