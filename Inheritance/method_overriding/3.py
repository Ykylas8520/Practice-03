class Person:
    def show(self):
        print("Person method")

class Student(Person):
    def show(self):
        print("Before parent")
        Person.show(self)
        print("After parent")

s = Student()
s.show()
