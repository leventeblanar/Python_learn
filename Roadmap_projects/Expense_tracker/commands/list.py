from .utils import read_expenses
from rich import print
from rich.table import Table
from rich.console import Console
from datetime import datetime

def list_all_expenses():

    expenses = read_expenses()
    if not expenses:
        print(f"[bold red]No expenses found[/bold red]")
        return


    table = Table(title="Expenses")
    table.add_column("Expense_id", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
    table.add_column("Description", style="green")
    table.add_column("Category", style="yellow")
    table.add_column("Amount", justify="right", style="red")

    for expense in expenses:
        date = datetime.fromisoformat(expense['date']).strftime("%Y-%m-%d")
        amount = f"{expense['amount']:.2f}"
        table.add_row(
            str(expense['id']),
            date,
            expense['description'],
            expense['category'],
            f"{amount}"
        )

    console = Console()
    console.print(table)
    
    