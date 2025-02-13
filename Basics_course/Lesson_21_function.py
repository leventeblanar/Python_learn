# function = A block of reusable code
#            place () after the function name to invoke it


def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"you are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

# happy_birthday("Levi", 31)
# happy_birthday("Andris", 45)
# happy_birthday("József", 21)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Levi", 42.50, "01/01")




# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def devide(x, y):
    z = x / y
    return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(devide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("levente", "blanár")

print(full_name)