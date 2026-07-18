from sqlalchemy.orm import Session
from decimal import Decimal

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    product: ProductCreate
):
    new_product = Product(
        name=product.name,
        price=product.price,
        stock=product.stock,
        category_id=product.category_id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product



def get_products(
    db: Session,
    page: int,
    limit: int,
    search: str | None = None,
    category_id: int | None = None,
    min_price: Decimal | None = None,
    max_price: Decimal | None = None
):

    query = db.query(Product)


    if search:
        query = query.filter(
            Product.name.ilike(f"%{search}%")
        )


    if category_id is not None:
        query = query.filter(
            Product.category_id == category_id
        )


    if min_price is not None:
        query = query.filter(
            Product.price >= min_price
        )


    if max_price is not None:
        query = query.filter(
            Product.price <= max_price
        )


    total = query.count()


    offset = (page - 1) * limit


    products = (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )


    return {
        "items": products,
        "total": total,
        "page": page,
        "limit": limit
    }



def get_product(
    db: Session,
    product_id: int
):

    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )



def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


    if not product:
        return None



    if product_data.name is not None:
        product.name = product_data.name


    if product_data.price is not None:
        product.price = product_data.price


    if product_data.stock is not None:
        product.stock = product_data.stock


    if product_data.category_id is not None:
        product.category_id = product_data.category_id



    db.commit()
    db.refresh(product)

    return product



def delete_product(
    db: Session,
    product_id: int
):

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


    if not product:
        return False


    db.delete(product)
    db.commit()

    return True