

# Quantum Book Store 

A simple object-oriented Python project that models an online bookstore with different types of books (Paper, EBook, Showcase). It supports adding books, removing outdated ones, and handling purchases with appropriate services for shipping and emailing.

---

## Features

*  **PaperBook**: Has stock, can be shipped to a physical address.
*  **EBook**: Has a filetype, can be sent via email.
*  **ShowcaseBook**: Not for sale, just a display item.
*  Add books with details: ISBN, title, author, year, price, quantity.
*  Remove outdated books (based on a maximum age in years).
*  Purchase a book (quantity, email, address required).
*  Simulated mail and shipping services.
*  Modular and easily extensible (can add more book types with minimal changes).

---

## Project Structure

* `Book (abstract)`: base class for all books.
* `PaperBook`, `EBook`, `ShowcaseBook`: subclasses implementing behavior.
* `Inventory`: manages book storage and operations.
* `MailService`, `ShippingService`: dummy service classes.
* `QuantumBookstoreFullTest`: test runner with sample data and actions.

---

## How to Run

1. Ensure Python 3.7+ is installed.
2. Save the code to a `.py` file (e.g., `quantum_bookstore.py`).
3. Run it:

```bash
python quantum_bookstore.py
```

---

## Sample Output

```
Quantum Book Store: Book 'Fiqh Al-Sunnah' added to inventory
Quantum Book Store: Book 'Ar-Raheeq Al-Makhtum' added to inventory
Quantum Book Store: Book 'Nahj al-Balagha' added to inventory
Quantum Book Store: Removed outdated book 'Nahj al-Balagha'
Quantum Book Store: PaperBook 'Fiqh Al-Sunnah' shipped to 456 Cairo St
Quantum Book Store: PaperBook 'Fiqh Al-Sunnah' shipped to 456 Cairo St
Quantum Book Store: Purchased 2x 'Fiqh Al-Sunnah' for $140.00
Quantum Book Store: EBook 'Ar-Raheeq Al-Makhtum' sent to reader2@example.com
Quantum Book Store: Purchased 1x 'Ar-Raheeq Al-Makhtum' for $40.00
Quantum Book Store: Showcase books are not for sale
```

---

## Example Test Books

| ISBN | Title                | Author                        | Type      | Year | Price | Qty |
| ---- | -------------------- | ----------------------------- | --------- | ---- | ----- | --- |
| 111  | Fiqh Al-Sunnah       | Sayyid Sabiq                  | PaperBook | 2005 | 70.0  | 10  |
| 222  | Ar-Raheeq Al-Makhtum | Safi-ur-Rahman al-Mubarakpuri | EBook     | 2012 | 40.0  | 5   |
| 333  | Nahj al-Balagha      | Imam Ali                      | Showcase  | 1998 | 0.0   | 0   |

---
<img width="495" alt="Screenshot 2025-07-09 at 5 00 41 PM" src="https://github.com/user-attachments/assets/3aa32b02-b244-4a8a-ad67-44602957984f" />


## Notes

* All printed messages are prefixed with `Quantum Book Store:`.
* ISBN is validated to be non-empty and alphanumeric.
* The code raises custom errors for out-of-stock or invalid books.

---

## License

This project is for educational and internship testing purposes.

---

