from pydantic import BaseModel,ConfigDict
from decimal import Decimal

class OrderItemResponse(BaseModel):
    id:int
    product_id: int
    product_name:str
    price:Decimal
    quantity:int
    model_config=ConfigDict(
        from_attributes=True
    )