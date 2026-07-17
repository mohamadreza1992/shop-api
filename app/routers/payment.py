from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.payment import PaymentResponse
from app.services.payment_service import create_payment
from app.dependencies.auth import get_current_user


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post(
    "/{order_id}",
    response_model=PaymentResponse
)
def pay_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_payment(
        db,
        order_id,
        current_user
    )