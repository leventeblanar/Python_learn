# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 25
temperature = 30

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b

print(min_num)
print(max_num)

status = "Adult" if age >= 18 else "Child"

weather = "Hot" if temperature > 20 else "Cold"

print(status)
print(weather)