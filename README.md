# 🏦 Bank Account App (Python OOP Project)

A simple object-oriented Python project that demonstrates the concepts of **Inheritance** and **Polymorphism** using a Bank Account system.

---

## 📌 Features

- Create a general bank account
- Deposit and withdraw money
- Create a savings account with interest
- Add interest to savings balance
- Display account details
- Demonstrates real-world OOP

---

## 📚 Concepts Used

- ✅ Classes & Objects  
- ✅ Inheritance  
- ✅ Polymorphism  
- ✅ Constructor Overriding  
- ✅ Method Overriding  
- ✅ Function Reusability

---

## 💼 Use Cases

- Mini apps for freelancing
- Basic finance or fintech-related apps
- Python OOP practice project
- Resume / GitHub portfolio project
  
---

##🛠️ Requirements
- Python 3.x
(Works on any system — Windows, Linux, or Mac)

---

## 🚀 How It Works

1. The `BankAccount` class handles normal banking operations.
2. The `SavingsAccount` class inherits from `BankAccount` and adds an `interest` feature.
3. Functions are used to show polymorphism by accepting different account types.

---

## 🧪 Example Usage

```python
acc1 = BankAccount("Ekta", 1000)
print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.display())

acc2 = SavingsAccount("Ekta", 2000)
print(acc2.add_interest())
