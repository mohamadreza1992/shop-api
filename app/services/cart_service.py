from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product
from app.models.user import User

from app.schemas.cart_item import CartItemCreate,CartItemUpdate
from app.core.errors import product_not_found,cart_not_found,cart_item_not_found


def get_or_create_cart(
    db: Session,
    user: User
) -> Cart:

    cart = db.query(Cart).filter(
        Cart.user_id == user.id
    ).first()

    if not cart:
        cart = Cart(
            user_id=user.id
        )

        db.add(cart)
        db.flush()

    return cart


def add_item_to_cart(
    db: Session,
    user: User,
    data: CartItemCreate
):

  
    cart = get_or_create_cart(
        db=db,
        user=user
    )


    
    product = db.query(Product).filter(
        Product.id == data.product_id
    ).first()

    if not product:
        product_not_found()


    cart_item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product.id
    ).first()


    if cart_item:
        cart_item.quantity += data.quantity

    else:
        
        cart_item = CartItem(
            cart_id=cart.id,
            product_id=product.id,
            quantity=data.quantity
        )

        db.add(cart_item)


    db.commit()
    db.refresh(cart_item)

    return cart_item


def get_user_cart(
    db: Session,
    user: User
):
    cart = db.query(Cart).filter(
        Cart.user_id == user.id
    ).first()

    if not cart:
       cart_not_found()

    return cart


def remove_cart_item(
    db: Session,
    user: User,
    item_id: int
):

    cart_item = db.query(CartItem).join(
        Cart
    ).filter(
        CartItem.id == item_id,
        Cart.user_id == user.id
    ).first()


    if not cart_item:
       cart_item_not_found()

    db.delete(cart_item)
    db.commit()

    return {
        "message": "Item removed successfully"
    }


def update_cart_item(
    db: Session,
    user: User,
    item_id: int,
    data: CartItemUpdate
):

    cart_item = db.query(CartItem).join(
        Cart
    ).filter(
        CartItem.id == item_id,
        Cart.user_id == user.id
    ).first()


    if not cart_item:
       cart_item_not_found()


    cart_item.quantity = data.quantity

    db.commit()
    db.refresh(cart_item)

    return cart_item