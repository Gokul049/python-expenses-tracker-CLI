# 💰 Python CLI Expense Tracker

A simple command-line Expense Tracker built using Python.
This application allows users to record, view, and manage daily expenses, and stores data in a CSV file for persistence.

---

## 🚀 Features

* ➕ Add new expenses
* 📋 View all expenses
* 🧮 Calculate total expenses
* 💾 Save expenses to CSV file
* 🔄 Load previous data automatically

---

## 🛠️ Technologies Used

* Python 3
* CSV File Handling (`csv` module)

---

## 📂 Project Structure

```id="m3k7h1"
expense_tracker.py
Expenses.csv   (auto-created)
```

---

## ▶️ How to Run

1. Make sure Python is installed
2. Run the script:

```id="w4bzjp"
python expense_tracker.py
```

---

## 🧠 How It Works

* Expenses are stored as a list of dictionaries:

```id="l2n9qp"
{"Name": "Food", "Amount": 100}
```

* Data is saved into `Expenses.csv` when exiting
* Data is loaded automatically when the program starts

---

## 📌 Menu Options

```id="aj6y9r"
1. Add Expense
2. Show Expense
3. Total Expense
4. Exit
```

---

## 💡 Example Usage

```id="d1gkz8"
Enter Choice : 1
Expense Name : Food
Expense Cost : 150
Expense Added ✔️

Enter Choice : 2
1. Food - ₹150.0
```

---

## ⚠️ Notes

* Ensure correct input format for amount (numbers only)
* The file `Expenses.csv` is created automatically if it doesn't exist
* Fix string formatting issue in code using single quotes inside f-strings

---

## 🔥 Future Improvements

* ❌ Delete expense option
* 🏷️ Add categories (Food, Travel, etc.)
* 📊 Expense analysis with charts
* 🎨 GUI version using Tkinter
* 📅 Filter by date/month

---

## 👨‍💻 Author

Developed by you 😎

---

## 📜 License

This project is open-source and free to use.
