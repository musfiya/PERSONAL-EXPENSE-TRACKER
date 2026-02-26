#this is your personal expense tracker
from datetime import datetime 
expenses=[]
def add_expense():
    date=input("enter date (YYYY-MM-DD) or press enter for today").strip()
    if not date:
        date=datetime.now().strftime("%Y-%m-%d")
    category=input("enter your category(food,Travel,rent,etc):").strip()
    amount=float(input("enter the amount "))
    note=input("enter note(optional):").strip()

    expense={
        "date": date,
        "category": category,
        "amount" : amount,
        "note" : note
    }

    expenses.append(expense)
    print("expense has been added successfully")
def view_expenses():
    if not expenses:
        print("no expenses has been recorded")
        return
    print("=*50")
    print(" ALL YOUR EXPENSES ARE ")
    print("="*50)
    for i,exp in enumerate(expenses,1):
        print(f"{i}.{exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")
def monthly_total():
    current_month=datetime.now().strftime("%Y-%m")
    total=0
    for exp in expenses:
        if exp["date"].startswith(current_month):
            total+=exp["amount"]
    print(f"Total spent this month : {total:.2f}")
def filter_by_category():
    chosen=input("enter the category to filter:") .strip().lower()
    found = False
    print(f" Expenses in {chosen}") 
    for exp in expenses:
        if exp["category"]==chosen:
            print(f"{exp['date']} | {exp["category"]} | {exp["amount"]} | {exp["note"]}")
            found = True
    if not found:
        print("no expenses found in this category")
def menu():
    print("="*50)
    print(" THIS IS YOUR PERSONAL EXPENSE TRACKER ")
    print("="*50)
    print("1.add an expense")
    print("2. view all the expenses")
    print("3. view monthly total")
    print("4.filter by category")
    print("5.exit")
def main():
    while True:
        menu()
        choice=input("choose an option (1-5): ")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            monthly_total()
        elif choice=="4":
            filter_by_category()
        elif choice=="5":
            break
        else:
            print("enter a valid choice to get started")
if __name__ == "__main__":
    main()
