from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.order import Order
from app.models.payment import Payment
from app.models.user import User


def create_payment(
    db: Session,
    order_id: int,
    user: User
) -> Payment:

    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    if order.payment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order already paid"
        )

    amount = sum(
        item.price * item.quantity
        for item in order.items
    )

    payment = Payment(
        order_id=order.id,
        amount=amount,
        status="success"
    )

    order.status = "paid"

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment