class LibraryManagementSystem:
    def __init__(self):
        self.library = []
        self.checked_out_books = []

    def add_book(self, book_title, author):
        book = {
            'title': book_title,
            'author': author,
            'available': True
        }
        self.library.append(book)
        print(f"Added '{book_title}' by {author} to the library.")

    def search_book(self, book_title):
        found_books = [book for book in self.library if book['title'] == book_title]
        if found_books:
            print(f"Found {len(found_books)} books with the title '{book_title}':")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, Status: {'Available' if book['available'] else 'Checked Out'}")
        else:
            print(f"No books with the title '{book_title}' were found in the library.")

   
# Create an instance of the library management system
library_system = LibraryManagementSystem()

# Example usage
library_system.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library_system.add_book("To Kill a Mockingbird", "Harper Lee")
library_system.search_book("The Great Gatsby")


