class Car:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print("Car brand:", self.brand)

c1 = Car("Toyota")
c1.info()
