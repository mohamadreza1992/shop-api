from decimal import Decimal
from fastapi import APIRouter, Depends,HTTPException,Query
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.schemas.product import ProductCreate , ProductResponse,MessageResponse,ProductUpdate,ProductListResponse
from app.services import product_service
from app.dependencies.permissions import require_admin
router = APIRouter(
    prefix="/products",
    tags=["products"]
)
@router.post("/",
             response_model=ProductResponse,
             dependencies=[Depends(require_admin)]
             )
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return product_service.create_product(db, product)

@router.get(
    "/",
    response_model=ProductListResponse
)
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    category_id:int | None=None,
    min_price: Decimal | None = Query(None,ge=0),
    max_price: Decimal | None = Query(None,ge=0),
    db: Session = Depends(get_db)

):
    return product_service.get_products(
        db,
        page,
        limit,
        search,
        category_id,
        min_price,
        max_price
    )


@router.get("/{product_id}", 
response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = product_service.get_product(
        db,
        product_id
    )
    if not product:
        raise HTTPException(
            status_code =404,
            detail="Product not found"
        )
    return product 


@router.put("/{product_id}",
            response_model=ProductResponse,
            dependencies=[Depends(require_admin)])
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated_product = product_service.update_product(
        db,
        product_id,
        product
    )

    if not updated_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated_product


@router.delete("/{product_id}",
               response_model=MessageResponse,
               dependencies=[Depends(require_admin)]
               )
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = product_service.delete_product(
        db,
        product_id
    )
    if not product:
         raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    
    return {
        "message": "Deleted successfully"
    }


