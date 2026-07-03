class Store:
    def __init__(self):
        self.products=[]
        self.counter=1
    def add_product(self,product):
        product.id=self.counter
        self.counter+=1
        self.products.append(product)
        return product        
    def get_products(self):
        return self.products
    def delete_product(self,product_id):
        for product in self.products:
            if product_id==product_id:
                self.products.remove(product)
                return True
        return False    
    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    def update_product(self, product_id, new_data):
        for product in self.products:
            if product.id == product_id:
                product.name = new_data.name
                product.price = new_data.price
                product.stock = new_data.stock
                return product
        return None
