import csv
import os
import pandas as pd
from datetime import datetime

# File to store expense related information
EXPENSE_FILE = 'expense.csv'

# Create file if not exists
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, mode='w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Category','Description','Amount'])


def add_expense(category, description, amount):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(EXPENSE_FILE,mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date,category,description,amount])
    print(f"Expense recorded:\nDate: {date}\nCategory: {category}\nDescription: {description}\nAmount{amount}\n")

def view_expenses():
    try:
        df = pd.read_csv(EXPENSE_FILE)
        print(df)
    except FileNotFoundError as e:
        print("No expense file found for view: ",e)

def view_summary():
    try:
        df = pd.read_csv(EXPENSE_FILE)
        summary = df.groupby("Category")["Amount"].sum()
        print("Amount spent on each category!")
        print(summary)
    except FileNotFoundError as e:
        print("No expense file found for summary stats: ",e)


if __name__ == "__main__":
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. View Summary")
        print("Any other key to exit.")

        choice = input("Choose an option.")

        if choice == "1":
            category = input("Enter category (e.g. Food, Travel, Grocery, Online Shopping, Miscillenous etc.): ")
            description = input("Enter description(Optional): ")
            amount = float(input("Enter amount"))
            add_expense(category,description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        else:
            print("Exiting the expense tracker. Goodbye!")
            break