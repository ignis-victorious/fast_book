#  ___________________
#  Import  LIBRARIES
from typing import Any
from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException

#  Import FILES
from book_db import books
from schema import Book, BookUpdate
#  OTHER
#  https://restfox.dev/
#  49.50
#  ___________________


app = FastAPI()


#  GET Web-Api Root
@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello this is the root of books"}


@app.get("/books")  # , response_model=list[Book])
async def get_all_books() -> list[dict[str, Any]]:  # -> list[Book]
    return books


#   POST: CREATE a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book: dict[str, Any] = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    print("_____________i am in!")
    for book in books:
        print(f"_____________book: {book}")
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")


@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["bublisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")


@app.get("/get_headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers


#
#  ___________________
#  Import  LIBRARIES
#  Import FILES
#  OTHERS
#  ___________________


# def main():
#     print("Hello from fast-book!")


# if __name__ == "__main__":
#     main()
