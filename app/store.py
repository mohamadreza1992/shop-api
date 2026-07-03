class Store:
    def __init__(self):
        self.products=[]
    def add_products(self,product):
        self.products.append(product)        
    def get_products(self):
        return self.products
