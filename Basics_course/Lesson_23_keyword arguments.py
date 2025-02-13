# keyword arguments = an argument preceeded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello(greeting="Hello", title="Mr.", first="Spongebob", last="Squarepants")  #this way the positioning does not matter, so we can mix up the order of this sequence but still have the correct outcome


# for x in range(1, 11):
#    print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=36, area=70, first=307, last=1340,)

print(phone_num)