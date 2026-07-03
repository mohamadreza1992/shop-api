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
@app.get("/products")
def list_products():
    return store.get_products()
@app.delete("/products/{product_id}")
def delete_products(product_id:int):
     result = store.delete_product(product_id)
     if result:
        return {"message": "Deleted successfully"}
     return {"message": "Product not found"}