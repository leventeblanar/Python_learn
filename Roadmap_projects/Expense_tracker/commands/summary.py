from rich import print
from rich.console import Console
from .utils import read_expenses, get_month_text
from datetime import datetime

def list_summary_of_expenses(month=None):

    expenses = read_expenses()

    if not expenses:
        print("[bold green]No expenses found[/bold green]")
        return
    
    if month is not None:
        filtered = []
        for e in expenses:
            try:
                if datetime.fromisoformat(e['date']).month == month:
                    filtered.append(e)
            except Exception:
                continue
        expenses = filtered
        if not expenses:
            print(f"[bold yellow]No expenses found for {get_month_text(month)}[/bold yellow]")
            return


    expense_total_sum = sum(expense['amount'] for expense in expenses)
    
    console = Console()
    title = f"Expense Summary{f' for {get_month_text(month)}' if month else ''}"
    console.print(f"[bold]{title}[/bold]")
    console.print(f"Total amount: [bold green]{expense_total_sum:.2f}[/bold green]")