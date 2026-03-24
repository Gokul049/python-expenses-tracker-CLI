import csv

expenses = []
def add_expense():
    name = input("Expense Name : ")
    amount = float(input("Expense Cost : "))
    expenses.append({"Name": name, "Amount": amount})
    print("Expense Added ✔️")

def show_expenses():
    if not  expenses:
        print("Expenses not add yet...")
    else:
        for i, expense in enumerate(expenses):
            print(f"{i+1}. {expense['Name']} - ₹{expense['Amount']}")

def total_expense():
    total = sum(expense["Amount"] for expense in expenses)
    print("Total Expenses :", total)

def save_expense():
    with open("Expenses.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Amount"])
        for expense in expenses:
            writer.writerow([expense["Name"], expense["Amount"]])

def  load_expense():
    try:
        with open("Expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({"Name": row["Name"],"Amount": float(row["Amount"]) })
    except:
        pass

load_expense()
while True:
    print("\n1. Add Expense.")
    print("2. Show Expense.")
    print("3. Total Expense.")
    print("4. Exit.")
    choice = input("Enter Choice : ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == "3":
        total_expense()
    elif choice == '4':
        save_expense()
        print("Expense saved, Existing...")
        break
    else:
        print("Invalid Choice 🥺")
