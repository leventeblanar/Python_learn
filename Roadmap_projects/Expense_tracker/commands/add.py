from .utils import read_expenses, write_expenses_json, now
from rich import print


def add_expense(category, description, amount):

    if amount <= 0:
        print("Amount must be [bold pink]greater[/bold pink] than 0.")
        return
    
    try:
        amount = float(amount)
        if round(amount, 2) != amount:
            raise ValueError("Amount must have at least two decimal places.")
    except Exception as e:
        print(f"[bold red]{e}[/bold red]")
        return
    
    expenses = read_expenses()


    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]['id'] + 1


    expenses.append({
        'id': expense_id,
        'date': now(),
        'description': description,
        'category': category,
        'amount': amount
    })

    write_expenses_json(expenses)
    print(f"Expense [bold green]added[/bold green] successfully. (ID: {expense_id})")