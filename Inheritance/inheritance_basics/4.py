class A:
    def method_a(self):
        print("A method")

class B(A):
    def method_b(self):
        print("B method")

class C(B):
    def method_c(self):
        print("C method")

c_obj = C()
c_obj.method_a()
c_obj.method_b()
c_obj.method_c()
