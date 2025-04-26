#  ___________________
#  Import  LIBRARIES
from pydantic import BaseModel
#  Import FILES
#  OTHERS
#  ___________________


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdate(Book):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
