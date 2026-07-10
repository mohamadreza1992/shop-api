from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductService:

    def add_product(self, db: Session, product: ProductCreate):

        new_product = Product(
            name=product.name,
            price=product.price,
            stock=product.stock
        )

        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product


    def get_products(self, db: Session):

        return db.query(Product).all()


    def get_product_by_id(self, db: Session, product_id: int):

        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )


    def delete_product(self, db: Session, product_id: int):

        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if product:
            db.delete(product)
            db.commit()
            return True

        return False


    def update_product(
        self,
        db: Session,
        product_id: int,
        product_data: ProductCreate
    ):

        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if product:
            product.name = product_data.name
            product.price = product_data.price
            product.stock = product_data.stock

            db.commit()
            db.refresh(product)

            return product

        return None    