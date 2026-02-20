class GrandParent:
    def hello(self):
        print("Hello from GrandParent")

class Parent(GrandParent):
    def hello(self):
        super().hello()
        print("Hello from Parent")

class Child(Parent):
    def hello(self):
        super().hello()
        print("Hello from Child")

ch = Child()
ch.hello()
