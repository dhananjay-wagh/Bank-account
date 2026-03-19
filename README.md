# VaultBank CLI System 🏦

A secure, object-oriented Command Line Interface (CLI) banking system built entirely in Python. This project demonstrates core backend engineering principles including persistent data storage, custom exception handling, and transaction auditing.

## 🚀 Features

* **Interactive CLI Menu:** Users can easily navigate through account creation, balance checking, deposits, and withdrawals.
* **Persistent File I/O:** User data (Name, Balance, Interest Rate) is securely saved to a local `.txt` file and automatically loaded when the application restarts.
* **Object-Oriented Architecture:** Built using clean OOP principles with separate `BankAccount` and `SavingsAccount` classes (Inheritance).
* **Data Encapsulation:** Account balances are protected using private variables (`__initial_balance`) to prevent direct, unauthorized modification.
* **Custom Security Traps:** Utilizes custom exceptions (`NegativeTransactionError`, `InsufficientFundsError`) to prevent invalid operations.
* **Automated Audit Logging:** Uses Python Decorators (`@transaction_logger`) to automatically log the start and success/failure of every transaction.
* **JSON Exporting:** Includes utility methods to export account data into cleanly formatted JSON strings.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Libraries:** `json`, `pathlib` (Standard Library)
* **Architecture:** Modular (Separated `main.py` execution from `blueprint.py` logic)

## 💻 How to Run

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Open your terminal and navigate to the project folder.
4. Run the main script:
   ```bash
   python main.py
