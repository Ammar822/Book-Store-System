from abc import ABC, abstractmethod
from datetime import datetime

# Dummy services
class MailService:
    @staticmethod
    def send(book, email):
        print(f"Quantum Book Store: EBook '{book.title}' sent to {email}")

class ShippingService:
    @staticmethod
    def send(book, address):
        print(f"Quantum Book Store: PaperBook '{book.title}' shipped to {address}")

# Custom Exceptions
class BookNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

# Base Book class
class Book(ABC):
    def __init__(self, isbn, title, author, year, price, quantity):
        if not isbn or not isbn.strip():
            raise ValueError("ISBN cannot be empty")
        if not isbn.isalnum():
            raise ValueError("ISBN must be alphanumeric")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.quantity = quantity

    def is_outdated(self, max_age):
        return datetime.now().year - self.year > max_age

    @abstractmethod
    def send_to(self, email, address):
        pass

    @abstractmethod
    def is_available(self):
        pass


class PaperBook(Book):
    def send_to(self, email, address):
        ShippingService.send(self, address)

    def is_available(self):
        return self.quantity > 0


class EBook(Book):
    def __init__(self, isbn, title, author, year, price, quantity, filetype):
        super().__init__(isbn, title, author, year, price, quantity)
        self.filetype = filetype

    def send_to(self, email, address):
        MailService.send(self, email)

    def is_available(self):
        return self.quantity > 0


class ShowcaseBook(Book):
    def send_to(self, email, address):
        raise Exception("Quantum Book Store: Showcase books are not for sale")

    def is_available(self):
        return False


class Inventory:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Quantum Book Store: Book with this ISBN already exists")
        self.books[book.isbn] = book
        print(f"Quantum Book Store: Book '{book.title}' added to inventory")

    def remove_outdated_books(self, max_age):
        to_remove = [isbn for isbn, book in self.books.items() if book.is_outdated(max_age)]
        for isbn in to_remove:
            book = self.books.pop(isbn)
            print(f"Quantum Book Store: Removed outdated book '{book.title}'")
        return to_remove

    def buy_book(self, isbn, quantity, email, address):
        if isbn not in self.books:
            raise BookNotFoundError("Quantum Book Store: Book not found")

        book = self.books[isbn]

        if not book.is_available():
            raise Exception("Quantum Book Store: Book is not available for sale")

        if book.quantity < quantity:
            raise OutOfStockError("Quantum Book Store: Not enough stock")

        total_price = book.price * quantity
        book.quantity -= quantity

        for _ in range(quantity):
            book.send_to(email, address)

        print(f"Quantum Book Store: Purchased {quantity}x '{book.title}' for ${total_price:.2f}")
        return total_price


# Testing class
class QuantumBookstoreFullTest:
    @staticmethod
    def run():
        store = Inventory()

        # Add books (Popular Arabic books)
        paper = PaperBook("111", "Fiqh Al-Sunnah", "Sayyid Sabiq", 2005, 70.0, 10)
        ebook = EBook("222", "Ar-Raheeq Al-Makhtum", "Safi-ur-Rahman al-Mubarakpuri", 2012, 40.0, 5, "pdf")
        demo = ShowcaseBook("333", "Nahj al-Balagha", "Imam Ali", 1998, 0.0, 0)

        store.add_book(paper)
        store.add_book(ebook)
        store.add_book(demo)

        # Remove outdated books
        store.remove_outdated_books(10)

        # Purchase book
        store.buy_book("111", 2, "reader1@example.com", "456 Cairo St")
        store.buy_book("222", 1, "reader2@example.com", "")

        # Attempt to buy demo book (should fail)
        try:
            store.buy_book("333", 1, "reader3@example.com", "")
        except Exception as e:
            print(e)


# Run tests
if __name__ == "__main__":
    QuantumBookstoreFullTest.run()
