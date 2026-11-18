# main.py
from models import Book, Magazine, DVD, Member, LibraryItem

# Create items of each type
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, 42)
dvd = DVD("Inception", 3, 148)

# Create members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
print("--- 1. Borrowing with error handling ---")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Trigger the borrow-limit error and the not-borrowed error, catching each
print("\n--- 2. Borrow-limit and not-borrowed error handling ---")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's borrow limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.return_item(dvd)  # should fail: Bob never borrowed the DVD
except ValueError as e:
    print("Could not return:", e)

# Return item successfully with late fee calculation
print("\n--- Return Item & Late Fee ---")
fee = alice.return_item(book, days_late=3)
print(f"Alice returned '{book.title}' (3 days late). Late fee charged: Rs {fee}")

# 3. Polymorphism: one loop, no type checks
print("\n--- 3. Polymorphism: mixed list late fee calculation ---")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("\n--- 4. Class attribute shared by all objects ---")
print("Total items created:", LibraryItem.total_items)

# 5. Encapsulation proof
print("\n--- 5. Encapsulation proof ---")
try:
    # Attempting to access private attribute directly
    print(book.__available)
except AttributeError as e:
    print("Accessing item.__available directly failed as expected:", e)

print("Accessing availability via is_available():", book.is_available())
print("Alice's current borrowed titles:", alice.borrowed_titles())
print("Bob's current borrowed titles:", bob.borrowed_titles())
