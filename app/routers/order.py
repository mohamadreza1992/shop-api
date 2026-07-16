from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.order import OrderResponse
from app.services.order_service import create_order,get_user_orders,get_order_by_id
from app.dependencies.auth import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse
)
def create_new_order(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    order = create_order(
        db=db,
        user=current_user
    )

    return order



@router.get(
    "",
    response_model=list[OrderResponse]
)
def get_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_user_orders(
        db,
        current_user
    )

@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_order_by_id(
        db,
        order_id,
        current_user
    )