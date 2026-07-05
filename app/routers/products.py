from fastapi import APIRouter
from app.schemas.products import ProductCreate
from app.services.product_service import ProductService

router = APIRouter()

service = ProductService()


@router.post("/products")
def create_product(product: ProductCreate):
    return service.add_product(product)


@router.get("/products")
def list_products():
    return service.get_products()


@router.get("/products/{product_id}")
def get_product(product_id: int):
    product = service.get_product_by_id(product_id)
    if product:
        return product
    return {"message": "Product not found"}


@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    result = service.delete_product(product_id)
    if result:
        return {"message": "Deleted successfully"}
    return {"message": "Product not found"}


@router.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate):
    updated = service.update_product(product_id, product)
    if updated:
        return {"message": "Updated successfully", "product": updated}
    return {"message": "Product not found"}