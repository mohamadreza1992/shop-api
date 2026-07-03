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
