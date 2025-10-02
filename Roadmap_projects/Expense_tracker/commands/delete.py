from .utils import read_expenses, write_expenses_json, now
from rich import print

def delete_expense(expense_id):

    expenses = read_expenses()
    if not expenses:
        print(f"[bold red]No expenses found.[/bold red]")

    if not any(expense['id'] == expense_id for expense in expenses):
        print(f"[bold red]Expense with id: {expense_id} not found.[/bold red]")
        return

    expenses = [expense for expense in expenses if expense['id'] != expense_id]
    write_expenses_json(expenses)
    print(f"[bold green]Expense deleted successfully![/bold green]")

