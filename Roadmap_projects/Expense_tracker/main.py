# Application should run from the command line and should have the following features:
# - Users can add an expense with a description and amount.
# - Users can update an expense.
# - Users can delete an expense.
# - Users can view all expenses.
# - Users can view a summary of all expenses.
# - Users can view a summary of expenses for a specific month (of current year).
# Here are some additional features that you can add to the application:
# - Add expense categories and allow users to filter expenses by category.
# - Allow users to set a budget for each month and show a warning when the user exceeds the budget.
# - Allow users to export expenses to a CSV file.

# Seen an example on using an argument parser for this project instead of user inputs so I will do this with it as well

# all credits to @siamonas

import argparse
from commands.add import add_expense
from commands.list import list_all_expenses
from commands.delete import delete_expense
from commands.summary import list_summary_of_expenses



#  created sub parsers for separate subcommands
parser = argparse.ArgumentParser(description='Expense Tracker')
subparser = parser.add_subparsers(dest='command', help='Sub-commands')


#  create parser for the "add" command
parser_add = subparser.add_parser('add', help='Add a new expense')
parser_add.add_argument('--category', required=True, type=str, help='Category of the expense')
parser_add.add_argument('--description', required=True, type=str, help='Description of the expense')
parser_add.add_argument('--amount', required=True, type=float, help='Amount of expense')

#  create parser for "list" command
parser_list = subparser.add_parser('list', help='List all expenses')

#  create parser for "summary" command
parser_summary = subparser.add_parser('summary', help='Sumamry of expenses')
parser_summary.add_argument('--month', required=False, type=int, choices=range(1, 13), help="Moth (1-12) to filter expenses")

#  create parser for "delete" command
parser_delete = subparser.add_parser('delete', help='Delete an expense')
parser_delete.add_argument('--id', required=True, type=int, help="ID of the expense to delete")

args = parser.parse_args()

match args.command:
    case 'add':
        add_expense(args.category, args.description, args.amount)
    case 'list':
        list_all_expenses()
    case 'summary':
        list_summary_of_expenses(args.month)
    case 'delete':
        delete_expense(args.id)
    case _:
        parser.print_help()