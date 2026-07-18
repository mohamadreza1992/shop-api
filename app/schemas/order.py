from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.order_item import OrderItemResponse
from app.models.enums import OrderStatus


class OrderResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    items: list[OrderItemResponse]

    model_config = ConfigDict(
        from_attributes=True
    )



class OrderStatusUpdate(BaseModel):
    status: OrderStatus    