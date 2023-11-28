class Book:
    def __init__(self, title, author, isbn, num_pages, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_pages = num_pages
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Price: Rs{self.price}")
        print("----------------------")

"""
book1 = Book("Python", "Naveed Khan", "444432-1", 350, 700)
book1.display_details()

book2 = Book("Data Science", "Naveed Khan", "387010-3", 500, 1000)
book2.display_details()

book1 = Book("Cyber Security", "Rijah", "2659856-7", 300, 1500)
book1.display_details()

book2 = Book("Soft Skills", "Mohsin", "3218978-5", 425, 750)
book2.display_details()
"""

class ReferenceBook(Book):
    def __init__(self, title, author, isbn, num_pages, price, ref_type):
        Book.__init__(self, title, author, isbn, num_pages, price)
        self.ref_type = ref_type

    def display_details(self):
        Book.display_details(self)
        print(f"Reference Type: {self.ref_type}")


class FictionBook(Book):
    def __init__(self, title, author, isbn, num_pages, price, genre):
        Book.__init__(self, title, author, isbn, num_pages, price)
        self.genre = genre

    def display_details(self):
        Book.display_details(self)
        print(f"Genre: {self.genre}")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def display_all_books(self):
        print("All Books in the Library:")
        for book in self.books.values():
            book.display_details()

    def search_book_by_title(self, title):
        if title in self.books:
            print(f"Book found. Details:")
            self.books[title].display_details()
        else:
            print("Book not found.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"{title} removed from the library.")
        else:
            print("Book not found in the library.")

    def print_all_books(self):
        print("Books available in the library:")
        for book_title in self.books:
            print(book_title)


library = Library()

reference_book = ReferenceBook("Python", "Naveed Khan", "444432-1", 350, 700, "Encyclopedia")
library.add_book(reference_book)

fiction_book = FictionBook("Data Science", "Naveed Khan", "387010-3", 500, 1000, "Classic")
library.add_book(fiction_book)

library.display_all_books()

library.search_book_by_title("Data Science")

library.remove_book("Python")

library.print_all_books()