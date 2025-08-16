import datetime

class Library:
    def __init__(self, books):
        self.books = books
        self.issued_books = {}  # {book_name: (borrower, issue_date)}

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"- {book}")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully!")

    def issue_book(self, book_name, borrower):
        if book_name in self.books:
            self.books.remove(book_name)
            issue_date = datetime.date.today()
            self.issued_books[book_name] = (borrower, issue_date)
            print(f"Book '{book_name}' issued to {borrower} on {issue_date}.")
        else:
            print("Sorry, book not available.")

    def return_book(self, book_name):
        if book_name in self.issued_books:
            borrower, issue_date = self.issued_books.pop(book_name)
            return_date = datetime.date.today()
            days_taken = (return_date - issue_date).days
            fine = 0
            if days_taken > 7:  # 7 days limit
                fine = (days_taken - 7) * 10
            self.books.append(book_name)
            print(f"Book '{book_name}' returned by {borrower}. Fine: ₹{fine}")
        else:
            print("This book was not issued.")

# ----------- Main Program ------------
library = Library(["Python Basics", "Data Science 101", "AI for Beginners"])

while True:
    print("\n--- Library Menu ---")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        book = input("Enter book name: ")
        library.add_book(book)
    elif choice == "3":
        book = input("Enter book name: ")
        borrower = input("Enter borrower name: ")
        library.issue_book(book, borrower)
    elif choice == "4":
        book = input("Enter book name: ")
        library.return_book(book)
    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
