from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

# Создание приложения FastAPI
app = FastAPI(title="Books API")

book_router = APIRouter(prefix="/api/v1", tags=["Books"])

class Book(BaseModel):
    id: int
    title: str
    author: str

# Имитация базы данных книг
books_db = [
    {"id": 1, "title": "Война и мир", "author": "Лев Толстой"},
    {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский"}
]

# Получение всех книг
@book_router.get("/books", response_model=List[Book])
def get_all_books():
    return books_db

# Получение книги по ID
@book_router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

# Создание новой книги
@book_router.post("/books", response_model=Book)
def create_book(book: Book):
    for existing in books_db:
        if existing["id"] == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book.model_dump())
    return book

# Удаление книги по ID
@book_router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book["id"] == book_id:
            del books_db[i]
            return {"message": "Книга удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")

app.include_router(book_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)