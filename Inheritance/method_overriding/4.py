class Vehicle:
    def info(self):
        print("Vehicle info")

class Car(Vehicle):
    def info(self):
        super().info()
        print("Car info")

c1 = Car()
c1.info()
