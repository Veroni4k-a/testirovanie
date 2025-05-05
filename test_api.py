import pytest
import httpx

# Базовый URL для тестирования API
BASE_URL = "http://127.0.0.1:8000/api/v1"

# Фикстура для создания тестового клиента
@pytest.fixture
def client():
    with httpx.Client(base_url=BASE_URL) as client:
        yield client

# Фикстура для сброса базы данных перед каждым тестом
@pytest.fixture(autouse=True)
def reset_database():
    from main import books_db
    books_db.clear()
    books_db.extend([
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой"},
        {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский"}
    ])

# Тест GET /books - Получение всех книг
def test_get_all_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Война и мир"
    assert data[1]["author"] == "Фёдор Достоевский"

# Тест GET /books/{book_id} - Получение книги по ID
def test_get_book_by_id(client):
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Война и мир"

# Тест GET /books/{book_id} - Книга не найдена
def test_get_book_not_found(client):
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Книга не найдена"

# Тест POST /books - Добавление новой книги
def test_create_book(client):
    new_book = {
        "id": 3,
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков"
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 3
    assert data["title"] == "Мастер и Маргарита"

    # Проверка, что книга добавлена в БД
    get_response = client.get("/books/3")
    assert get_response.status_code == 200

# Тест POST /books - Книга с таким ID уже существует
def test_create_book_duplicate_id(client):
    new_book = {
        "id": 1,  # ID, который уже есть в базе
        "title": "Ошибка",
        "author": "Тест"
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 400
    assert response.json()["detail"] == "Книга с таким ID уже существует"

# Тест POST /books - Невалидный запрос (отсутствуют поля)
def test_create_book_invalid_data(client):
    invalid_book = {
        "id": 4,
        "title": "Без автора"
    }
    response = client.post("/books", json=invalid_book)
    assert response.status_code == 422  # Ошибка валидации Pydantic

# Тест DELETE /books/{book_id} - Удаление книги
def test_delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Книга удалена"

    # Проверка, что книга удалена
    get_response = client.get("/books/1")
    assert get_response.status_code == 404

# Тест DELETE /books/{book_id} - Книга не найдена
def test_delete_book_not_found(client):
    response = client.delete("/books/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Книга не найдена"