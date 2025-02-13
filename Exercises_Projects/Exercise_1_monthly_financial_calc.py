# --- User input ---
income = float(input("Please enter your monthly salary: "))
rent = float(input("Please enter your monthly rent: "))
groceries_expense = float(input("How much do you spend on groceries a month?: "))
entertainment_expense = float(input("How much do you spend on going out in a month?: "))
other_expense = float(input("Do you have any other expenses? If so, please enter their mothly cost: "))

# --- Calculations ---
total_expenses = rent + groceries_expense + entertainment_expense + other_expense
monthly_savings = income - total_expenses

# --- Output ---
print(f"\nTotal monthly expenses: ${total_expenses:.2f}")
if monthly_savings > 0:
    print(f"Congratulations, you saved ${monthly_savings:.2f}!")
else:
    print(f"Sadly, this month you lost {-monthly_savings:.2f}")