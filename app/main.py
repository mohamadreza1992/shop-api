from fastapi import FastAPI
from app.schemas import ProductCreate
from app.store import Store

app= FastAPI()
store=Store()

@app.get("/")
def home():
    return{"message":"first routh "}

@app.post("/products")
def create_product(product: ProductCreate):
    store.add_product(product)
    return {"message": "Product added successfully"}