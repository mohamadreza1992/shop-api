from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db

from app.schemas.cart_item import CartItemCreate, CartItemResponse,CartItemUpdate

from app.services.cart_service import add_item_to_cart

from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.cart import CartResponse
from app.services.cart_service import get_user_cart
from app.services.cart_service import remove_cart_item,update_cart_item

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post(
    "/items",
    response_model=CartItemResponse
)
def add_cart_item(
    data: CartItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    cart_item = add_item_to_cart(
        db=db,
        user=current_user,
        data=data
    )

    return cart_item


@router.get(
    "",
    response_model=CartResponse
)
def get_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_cart(
        db=db,
        user=current_user
    )


@router.delete("/items/{item_id}")
def delete_cart_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return remove_cart_item(
        db=db,
        user=current_user,
        item_id=item_id
    )




@router.patch(
    "/items/{item_id}",
    response_model=CartItemResponse
)
def update_item(
    item_id: int,
    data: CartItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return update_cart_item(
        db=db,
        user=current_user,
        item_id=item_id,
        data=data
    )