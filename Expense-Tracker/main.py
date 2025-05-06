import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Create the CSV file with headers if it doesn't exist
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date/Time", "Amount", "Category", "Note"])

# Add a new expense entry to the CSV
def add_expense(amount, category, note):
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount, category, note])
    print("✅ Expense added!")

# Display all recorded expenses
def view_expenses():
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    print(f"{' | '.join(row)}")
                    print("-" * 50)
                else:
                    print(f"{' | '.join(row)}")
    except FileNotFoundError:
        print("❌ No expenses found.")

# Main interaction loop
if __name__ == "__main__":
    initialize_file()
    print("💰 Expense Tracker")
    
    while True:
        choice = input("\nEnter (1) Add Expense (2) View Expenses (3) Exit: ")

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category (e.g., food, transport): ")
            note = input("Note (optional): ")
            add_expense(amount, category, note)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting... Stay financially smart!")
            break
        else:
            print("❗ Invalid input. Try again.")