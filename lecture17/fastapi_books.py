import csv
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from flask_books import load_books, find_book


app = FastAPI()

class Book(BaseModel):
    Title: str
    Author: str
    Genre: str
    Height: int
    Publisher: str

@app.get('/books/{title}')
def get_book(title: str):
    books = load_books()
    book = find_book(books, title)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    return book

@app.post('/books')
def add_book(book: Book):
    with open('books.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([book.Title, book.Author, book.Genre, 
                        book.Height, book.Publisher])
        return {'status': 'added', 'book': book}


if __name__ == "__main__":
    print("Run with: fastapi dev fastapi_books.py")  # cd lecture17
