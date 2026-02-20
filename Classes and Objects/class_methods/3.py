class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, "grade is", self.grade)

s1 = Student("Dias", "A")
s1.show()
