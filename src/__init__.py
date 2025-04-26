#  ___________________
#  Import  LIBRARIES
from fastapi import FastAPI

#  Import FILES
from src.books.routes import book_router
#  OTHER
#  https://restfox.dev/
#  1:23:45
#  ___________________

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
