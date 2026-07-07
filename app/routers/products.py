from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductCreate
from app.services.product_service import ProductService


router = APIRouter()

service = ProductService()


@router.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return service.add_product(db, product)


@router.get("/products")
def list_products(
    db: Session = Depends(get_db)
):
    return service.get_products(db)


@router.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = service.get_product_by_id(
        db,
        product_id
    )

    if product:
        return product

    return {"message": "Product not found"}


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    result = service.delete_product(
        db,
        product_id
    )

    if result:
        return {"message": "Deleted successfully"}

    return {"message": "Product not found"}


@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    updated = service.update_product(
        db,
        product_id,
        product
    )

    if updated:
        return updated

    return {"message": "Product not found"}