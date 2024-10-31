from datetime import datetime
import csv
import os
filename = r"C:\Users\shalini\Desktop\AIMLprojects\PersonalExpenseTracker\expenses.csv";
# validate date
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True  
    except ValueError:
        return False  
# Store the expense in a list as a dictionary   
def get_expense_details():
       while True:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        
        if not validate_date(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue  
        category = input("Enter the category of the expense: ")
        amount = input("Enter the amount spent: ")
        description = input("Enter a brief description of the expense: ")
        expense_details = {
                "date": date,
                "category": category,
                "amount": amount,
                "description": description
                }
        return expense_details
expenses = [get_expense_details()]

#Display expense
def display_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    for expense in expenses:
        # Validate that all required fields are present
        if isinstance(expense, dict):
            date = expense.get("date")
            category = expense.get("category")
            amount = expense.get("amount")
            description = expense.get("description")
        
            if not all([date, category, amount, description]):
                print("Incomplete entry found; skipping...")
                continue  # Skip this entry if any required details are missing
            
            # Display the valid expense details
            print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")
        else:
            print("Invalid entry; expected a dictionary.")

display_expenses(expenses)


def save_expenses_to_csv(expenses, filename):
    """Saves the list of expenses to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])  # Write header
        for expense in expenses:
            writer.writerow([expense["date"], expense["category"], expense["amount"], expense["description"]])

def load_expenses_from_csv(filename):
    """Loads expenses from a CSV file and returns a list of expenses."""
    expenses = []
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"]) if row["amount"] else 0.0
                expenses.append(row)
    return expenses


# Monthly Budget
def input_monthly_budget():
    while True:
        try:
            budget = float(input("Enter your total budget for the month: "))
            if budget < 0:
                print("Please enter a positive amount.")
            else:
                return budget
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Calculate total expenses
def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        amount = expense.get("amount")
        if amount is not None:
            total += float(amount)
    return total

# compare budget and expenses
def compare_budget_and_expenses(budget, expenses):
    total_expenses = calculate_total_expenses(expenses)
    print(f"Total Expenses: {total_expenses}")

    if total_expenses > budget:
        print("You have exceeded your budget!")
    else:
        remaining_balance = budget - total_expenses
        print(f"You have {remaining_balance} left for the month.")

def add_expense():
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    category = input("Enter the category of the expense: ")
    amount = input("Enter the amount spent: ")
    description = input("Enter a brief description of the expense: ")
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    
    expenses.append(expense)
    print("Expense added.")


def view_expenses():
    if not expenses:
        print("No expenses to display.")
    else:
        print("Expenses:")
        for expense in expenses:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

def display_menu():
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")

def main():
    global expenses
    expenses = load_expenses_from_csv(filename)  # Load existing expenses from CSV at start

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_budget = input_monthly_budget()
            compare_budget_and_expenses(monthly_budget, expenses)
        elif choice == '4':
            save_expenses_to_csv(expenses, filename)
            print("Expenses saved.")
        elif choice == '5':
            save_expenses_to_csv(expenses, filename)
            print("Expenses saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
