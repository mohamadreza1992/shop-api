from pydantic import BaseModel, ConfigDict
from app.schemas.category import CategoryResponse


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    category_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: CategoryResponse | None = None

    model_config = ConfigDict(
        from_attributes=True
    )


class MessageResponse(BaseModel):
    message: str


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    stock: int | None = None