# Campus Library Manager

A Python-based library management system demonstrating Object-Oriented Programming (OOP) principles including abstraction, inheritance, polymorphism, encapsulation, and robust exception handling.

---

## Deliverables & Reflection Questions

### 1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?
`LibraryItem` is an abstract base class (inheriting from `abc.ABC`) because it models a generic item that should never be instantiated directly; it serves as a common contract for concrete item types. If a subclass like `DVD` forgets to implement the `@abstractmethod` `late_fee()`, Python treats `DVD` as an abstract class as well and raises a `TypeError` at instantiation time (`Can't instantiate abstract class DVD without an implementation for abstract method 'late_fee'`). This enforces at development time that every distinct item type defines its own specific fee calculation logic.

### 2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?
Accessing `item.__available` from outside the class raises an `AttributeError` because Python's name mangling prefixes private attributes with `_ClassName` (becoming `_LibraryItem__available`). We use the public getter method `is_available()` to preserve encapsulation, ensuring the item's internal availability state is read-only from the outside and can only be altered through designated methods (`mark_borrowed()` and `mark_returned()`). This prevents external components from corrupting the internal state or bypassing borrowing rules.

### 3. What is the difference between `LibraryItem.total_items` and `self.title`?
`LibraryItem.total_items` is a class attribute shared across the class and all of its instances, maintaining a global count of how many items have been created. In contrast, `self.title` is an instance attribute unique to each individual object created from a class. Changes to a class attribute reflect across the entire class hierarchy, whereas modifying `self.title` affects only that specific instance.

---

## Project Structure

```text
CampusLibraryManager/
├── models.py        # Domain models: LibraryItem (abstract), Book, Magazine, DVD, Member
├── main.py          # Demonstration script exercising OOP concepts & error handling
├── output.txt       # Captured console output of the final demonstration run
├── project.md       # Project brief and specification
└── README.md        # Documentation and answers to review questions
```

---

## Running the Program

Run the demonstration script using Python 3.12 or later:

```bash
python3 main.py
```
