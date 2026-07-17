from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: Decimal
    status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )