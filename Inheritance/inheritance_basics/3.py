class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def show_brand(self):
        print("Car brand is", self.brand)

c1 = Car("Toyota")
c1.show_brand()
