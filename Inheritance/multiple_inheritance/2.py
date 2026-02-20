class X:
    def x_method(self):
        print("X method")

class Y:
    def y_method(self):
        print("Y method")

class Z(X, Y):
    def z_method(self):
        print("Z method")

z = Z()
z.x_method()
z.y_method()
z.z_method()
