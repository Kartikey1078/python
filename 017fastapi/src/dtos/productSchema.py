from pydantic import BaseModel

class CreateProduct(BaseModel):
    name:str
    price:int 
    category:str
    stock:int 