from decimal import Decimal
from pydantic import BaseModel, ConfigDict,Field
from app.schemas.category import CategoryResponse
from typing import List

class ProductCreate(BaseModel):
    name: str = Field(min_length=2,max_length=100)
    price: Decimal= Field(gt=0)
    stock: int = Field(ge=0)
    category_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    stock: int
    category: CategoryResponse | None = None

    model_config = ConfigDict(
        from_attributes=True
    )


class MessageResponse(BaseModel):
    message: str


class ProductUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,

    )
    price: Decimal | None = Field(default=None,gt=0)
    stock: int | None = Field(default=None,ge=0)
    category_id: int | None = None


class ProductListResponse(BaseModel):
    items:List[ProductResponse]
    total: int
    page: int
    limit: int    