# *args         = allows ypou to pass multiple non-key arguments
# **kwargs      = allows you to pass multiple keyword-arguments
#               * unpacking opreator
#               1. positional 2. default 3. keyword 4. ARBITRARY

def add(*args):   # the parameter is a tuple in this case, through which we can iterate
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1, 2, 3)) - we can add as many elements as we want this way because the for loop will iterate through it and add it to the total


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_address(street="123 Fake street", 
#              city="Detroit", 
#              state="MI", 
#              zip="54123")




def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs: 
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
              
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
               street="123 Fake street", 
               city="Detroit",
               apt="",
               pobox="PO box #1001",
               state="MI", 
               zip="54123")