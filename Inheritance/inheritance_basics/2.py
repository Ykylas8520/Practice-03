class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def study(self):
        print("Studying...")

s1 = Student()
s1.greet()
s1.study(
