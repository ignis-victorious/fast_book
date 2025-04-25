#  ___________________
#  Import  LIBRARIES
from pydantic import BaseModel
#  Import FILES
#  OTHERS
#  ___________________




class BookCreate(BaseModel) :
    title : str 
    author : str



# {
#     "title": "Learn Django",
#     "author": "Elle Emagnu"
# }