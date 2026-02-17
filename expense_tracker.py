import csv
from datetime import datetime
FILE_NAME="expenses.csv"
def add_expense():
    amount=input("Enter amount:")
    category=input("Enter category(Foof, Travel,etc): ")
    description=input("Enter description: ")
    date= datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME,"a", newline="") as file:
        writer= csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("Expenses added\n ")
def view_expenses():
    try:
        with open(FILE_NAME,"r")as file:
            reader=csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found\n")
def total_expense():
    total=0
    try:
        with open(FILE_NAME,"r")as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"Total Spent: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses found.\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
