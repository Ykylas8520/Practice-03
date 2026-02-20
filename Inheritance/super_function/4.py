class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

c_obj = C()
c_obj.method_a()
c_obj.method_b()
c_obj.method_c()
