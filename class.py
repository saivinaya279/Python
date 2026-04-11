# Create class Car with attributes
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c1 = Car("BMW", 5000000)
print(c1.brand, c1.price)