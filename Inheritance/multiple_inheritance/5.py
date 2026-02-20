class GrandParent:
    def greet(self):
        print("Hello from GrandParent")

class ParentA(GrandParent):
    def greet(self):
        super().greet()
        print("Hello from ParentA")

class ParentB:
    def greet(self):
        print("Hello from ParentB")

class Child(ParentA, ParentB):
    def greet(self):
        super().greet()
        print("Hello from Child")

ch = Child()
ch.greet()
