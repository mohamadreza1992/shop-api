from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.models.cart import Cart
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.user import User
from app.models.product import Product




def create_order(
    db: Session,
    user: User
) -> Order:

    cart = db.query(Cart).filter(
        Cart.user_id == user.id
    ).first()

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart not found"
        )
    
    if not cart.items:
            raise HTTPException(
            status_code=400,
            detail="Cart is empty"
        )
    
    order = Order(
        user_id=user.id,
        status="pending"
    )

    db.add(order)
    db.flush()


    for item in cart.items:

        product = item.product

        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock for {product.name}"
            )

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            product_name=product.name,
            price=product.price,
            quantity=item.quantity
        )

        product.stock -= item.quantity

        db.add(order_item)



    for item in cart.items:
        db.delete(item)


    
    db.commit()
    db.refresh(order)

    return order


def get_user_orders(
    db: Session,
    user: User
)->list[Order]:

    orders = db.query(Order).filter(
        Order.user_id == user.id
    ).all()

    return orders



def get_order_by_id(
    db: Session,
    order_id: int,
    user: User
) -> Order:

    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    return order