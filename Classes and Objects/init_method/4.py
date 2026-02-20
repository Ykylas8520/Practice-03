class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

b1 = Book("Math", 5000)
print(b1.title, b1.price)
