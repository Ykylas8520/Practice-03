class P1:
    def hello(self):
        print("Hello from P1")

class P2:
    def hello(self):
        print("Hello from P2")

class C(P1, P2):
    def hello(self):
        super().hello()
        print("Hello from C")

c = C()
c.hello()
