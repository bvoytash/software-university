from project.product import Product

class Drink(Product):
    def __init__(self, name):
        super().__init__(name, 10)
        self.quantity = 10
        # self.quantity = quantity
