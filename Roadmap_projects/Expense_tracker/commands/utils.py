import json
import os
from datetime import datetime

EXPENSE_FILE = 'expenses.json'

# todays date, time
def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#  read expense file
def read_expenses():

    if not os.path.exists('expenses.json'):
        return []
    
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Json file is corrupt.")


# write json file
def write_expenses_json(expenses):
    with open("expenses.json", "w") as f_out:
        json.dump(expenses, f_out, indent=4, ensure_ascii=False)


#  write csv file
def export_to_csv(expenses):
    with open("expenses.csv", "w") as file:
        file.write(expenses)


def get_month_text(month):

    return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][month - 1] if month else ""

