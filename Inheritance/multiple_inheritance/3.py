class Parent1:
    def show(self):
        print("Parent1 show")

class Parent2:
    def show(self):
        print("Parent2 show")

class Child(Parent1, Parent2):
    def show(self):
        print("Child show")

ch = Child()
ch.show()
