from app.schemas.products import ProductCreate


class ProductService:
    def __init__(self):
        self.products = []
        self.counter = 1

    def add_product(self, product: ProductCreate):
        new_product = product.model_dump()
        new_product["id"] = self.counter
        self.counter += 1

        self.products.append(new_product)
        return new_product

    def get_products(self):
        return self.products

    def get_product_by_id(self, product_id: int):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    def delete_product(self, product_id: int):
        for product in self.products:
            if product["id"] == product_id:
                self.products.remove(product)
                return True
        return False

    def update_product(self, product_id: int, product_data: ProductCreate):
        for product in self.products:
            if product["id"] == product_id:
                product["name"] = product_data.name
                product["price"] = product_data.price
                product["stock"] = product_data.stock
                return product
        return None