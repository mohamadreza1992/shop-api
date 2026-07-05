from fastapi import FastAPI
from app.routers.products import router as products_router

app = FastAPI(title="Shop API")


# Router injection
app.include_router(products_router)