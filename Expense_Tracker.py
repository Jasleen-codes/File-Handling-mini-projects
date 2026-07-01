# Expense_tracker
import os

file = "expenses.txt"

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        with open(file, "a") as f:
            f.write(f"{date},{category},{amount}\n")

        print("Expense Added Successfully!")

    elif choice == "2":
        if os.path.exists(file):
            with open(file, "r") as f:
                print("\nDate\t\tCategory\tAmount")
                print("-------------------------------------")
                print(f.read())
        else:
            print("No expense records found.")

    elif choice == "3":
        total = 0

        if os.path.exists(file):
            with open(file, "r") as f:
                for line in f:
                    date, category, amount = line.strip().split(",")
                    total += float(amount)

            print("Total Expense = ₹", total)
        else:
            print("No expense records found.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")