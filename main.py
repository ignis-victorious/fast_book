
#  ___________________
#  Import  LIBRARIES
from fastapi import FastAPI, Header
#  Import FILES
from schema import BookCreate
#  OTHER
#  https://restfox.dev/
#  ___________________





app = FastAPI ()



@app. get ('/')
async def read_root() -> dict[str, str]:
    return {"message": "Hello World" }


#  GET PATH->name
# @app.get ('/greet/{name}')
# async def path_greet_name (name: str) -> dict[str, str] :
#     return { "message" : f"Hello {name}"}

#  GET QUERY->name
# @app.get ('/greet')
# async def query_greet_name (name: str) -> dict[str, str] :
#     return { "message" : f"Hello {name}"}

#  GET PATH->name  and QUERY->age 
# @app.get ('/greet/{name}')
# async def p_and_q_greet (name: str|None = "User", age:int|None =None ) -> dict[str, str] :
#     if age:
#         return { "message" : f"Hello {name} you are only {age} years old!"}
#     return { "message" : f"Hello {name}."}


#  QUERY - GET either or both name and age 
@app.get ('/greet')
async def all_q_greet (name: str|None = "User", age:int|None =None ) -> dict[str, str] :
    if age:
        return { "message" : f"Hello {name} you are only {age} years old!"}
    return { "message" : f"Hello {name}."}


#   POST a new book
@app.post('/create_book')
async def create_book(book_data:BookCreate)  -> dict[str, str]:
    return {"title": book_data.title,"author": book_data.author}


@app.get('/get_headers', status_code=200)
async def get_headers(accept:str = Header (None),
    
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
    ):

    request_headers = {}

    request_headers ["Accept"] = accept
    request_headers ["Content-Type"] = content_type
    request_headers ["User-Agent"] = user_agent
    request_headers ["Host"] = host
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
