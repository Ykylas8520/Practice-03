class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
