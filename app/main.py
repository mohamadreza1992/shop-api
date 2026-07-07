from fastapi import FastAPI

from app.database import engine, Base
from app.models import product

from app.routers.products import router as products_router


app = FastAPI(title="Shop API")


Base.metadata.create_all(bind=engine)


app.include_router(products_router)