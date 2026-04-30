import asyncio
from typing import Dict, List

# Simulated database of books
books: Dict[int, Dict[str, object]] = {
    101: {
        "id": 101,
        "title": "Introduction to Python",
        "author": "John Doe",
        "category": "Programming",
        "available": True
    },
    102: {
        "id": 102,
        "title": "Database Systems",
        "author": "Jane Smith",
        "category": "Computing",
        "available": True
    }
}

# Loan records storage
loans: List[Dict[str, object]] = []


# POST /loans (borrow book)
async def borrow_book(user_id: int, book_id: int) -> str:
    print(f"User {user_id} is borrowing book {book_id}")

    await asyncio.sleep(5)  # 5 seconds delay

    book = books.get(book_id)

    if book is None:
        return "Book not found"

    if book["available"] is False:
        return "Book already borrowed"

    book["available"] = False

    loan = {
        "loan_id": len(loans) + 1,
        "user_id": user_id,
        "book_id": book_id,
        "status": "borrowed"
    }

    loans.append(loan)

    return f"Borrow successful! Loan ID = {loan['loan_id']}"


# PUT /loans/return (return book)
async def return_book(loan_id: int) -> str:
    print(f"Processing return for loan {loan_id}...")

    await asyncio.sleep(10)  # 10 seconds delay

    for loan in loans:
        if loan["loan_id"] == loan_id:
            loan["status"] = "returned"

            book_id = loan["book_id"]
            books[book_id]["available"] = True

            return f"Book {book_id} returned successfully"

    return "Loan not found"


# GET /overdue (simulated task)
async def check_overdue() -> str:
    print("Checking overdue books...")

    await asyncio.sleep(15)  # 15 seconds delay

    return "No overdue books found"


# Simulating multiple users
async def main() -> None:
    print("Task 1 starting now (Borrow Book 101)")
    print("Task 2 starting now (Borrow Book 102)")
    print("Task 3 starting now (Return Loan 1)")

    results = await asyncio.gather(
        borrow_book(1, 101),
        borrow_book(2, 102),
        return_book(1)
    )

    print("\n--- TASKS COMPLETED ---")

    print("Task 1 ended in 5 seconds")
    print("Task 2 ended in 5 seconds")
    print("Task 3 ended in 10 seconds")

    print("\n--- RESULTS ---")
    for result in results:
        print(result)


asyncio.run(main())
