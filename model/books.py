import imp
from pydantic import BaseModel

class Bookdetail(BaseModel):
        TITLE: str 
        PRICE: int
        AUTHOR: str | None=None


