from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.models.user import User

from app.schemas.order import (
    OrderResponse,
    OrderStatusUpdate
)

from app.services.order_service import (
    create_order,
    get_user_orders,
    get_order_by_id,
    get_all_orders,
    update_order_status
)

from app.dependencies.auth import get_current_user
from app.dependencies.permissions import require_admin


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)




@router.get(
    "/admin/all",
    response_model=list[OrderResponse],
    dependencies=[Depends(require_admin)]
)
def admin_get_orders(
    db: Session = Depends(get_db)
):

    return get_all_orders(db)



@router.patch(
    "/admin/{order_id}/status",
    response_model=OrderResponse,
    dependencies=[Depends(require_admin)]
)
def admin_update_order_status(
    order_id: int,
    data: OrderStatusUpdate,
    db: Session = Depends(get_db)
):

    return update_order_status(
        db,
        order_id,
        data.status
    )





@router.post(
    "",
    response_model=OrderResponse
)
def create_new_order(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_order(
        db=db,
        user=current_user
    )



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