from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int

    class Config:
        from_attributes = True    

class MessageResponse(BaseModel):
    message: str

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    stock: int | None = None    