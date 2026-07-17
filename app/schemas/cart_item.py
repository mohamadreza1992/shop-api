from pydantic import BaseModel, ConfigDict, Field


class CartItemCreate(BaseModel):

    product_id: int

    quantity: int = Field(
        ge=1
    )


class CartItemResponse(BaseModel):

    id: int
    product_id: int
    quantity: int

    model_config = ConfigDict(
        from_attributes=True
    )


class CartItemUpdate(BaseModel):

    quantity: int = Field(
        ge=1
    )