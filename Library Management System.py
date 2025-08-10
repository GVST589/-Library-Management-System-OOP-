class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        print(f"📖 {self.title} by {self.author} — Copies: {self.copies}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies=1):
        for book in self.books:
            if book.title == title and book.author == author:
                book.copies += copies
                print(f"✅ Added {copies} more copies of {title}")
                return
        self.books.append(Book(title, author, copies))
        print(f"🎉 New book '{title}' added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.copies > 0:
                book.copies -= 1
                print(f"📚 You borrowed '{title}'. Enjoy reading!")
                return
        print("❌ Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.copies += 1
                print(f"✅ You returned '{title}'. Thank you!")
                return
        print("❌ This book does not belong to our library.")

    def view_books(self):
        if not self.books:
            print("📭 No books available in the library.")
        else:
            print("\n📚 Library Collection:")
            for book in self.books:
                book.display()

#=====================
# Main Program
#=====================

if __name__ == "__main__":
    library = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            copies = int(input("Number of Copies: "))
            library.add_book(title, author, copies)

        elif choice == "2":
            title = input("Book Title: ")
            library.borrow_book(title)

        elif choice == "3":
            title = input("Book Title: ")
            library.return_book(title)

        elif choice == "4":
            library.view_books()

        elif choice == "5":
            print("👋 Thank you for visiting the library!")
            break

        else:
            print("❌ Invalid choice.")
