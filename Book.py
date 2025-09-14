class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is currently not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

Book1 = Book("1984", "George Orwell", "1234567890")
Book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
member1 = Member("Alice", "M001")

print("Book Information:")
Book1.display_info()
Book2.display_info()
print("\nMember Actions:")
member1.borrow_book(Book1)

class StaffMember:
    def __init__(self, name, staff_id, member_id,):
        self.name = name
        self.staff_id = staff_id
        self.member_id = member_id

    def display_info(self):
        print(f"Name: {self.name}, Staff ID: {self.staff_id}, Member ID: {self.member_id}")
staff1 = StaffMember("Bob", "S001", "M002")
staff1.display_info()
member1.return_book(Book1)
