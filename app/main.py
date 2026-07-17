from fastapi import FastAPI

from app.routers.products import router as products_router
from app.routers.categories import router as categories_router
from app.routers.auth import router as auth_router
from app.routers.cart import router as cart_router
from app.routers.order import router as order_router
from app.routers.payment import router as payment_router

app = FastAPI(title="Shop API")

app.include_router(products_router)
app.include_router(categories_router)
app.include_router(auth_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(payment_router)