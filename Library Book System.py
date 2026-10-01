class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)
    def borrow(self):
        if self.available :
            print("Book borrowed successfully!")
            self.available = False
        else:
            print("Book is not available!")
    def return_book(self):
        if not self.available:
           self.available = True 
           print("Book returned successfully!")
        else:
            print("Book is already in the library.")

s1 = Book("Python Basics", "Harry", True)
s1.display()
s1.borrow()
s1.display()
s1.return_book()
s1.display()

    