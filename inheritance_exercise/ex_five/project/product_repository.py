from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
        # Here you can reuse the self.find() function

    def __repr__(self):
        res = '\n'.join([f'{product.name}: {product.quantity}' for product in self.products])
        return res