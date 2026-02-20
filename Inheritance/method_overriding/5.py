class A:
    def message(self):
        print("A message")

class B(A):
    def message(self):
        super().message()
        print("B message")

class C(B):
    def message(self):
        super().message()
        print("C message")

c_obj = C()
c_obj.message()
