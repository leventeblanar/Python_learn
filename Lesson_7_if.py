# if = Do some code only IF some condition is True
#      Else do something else


# Example 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("You must be 18+ years old to sign up!")

# Example 2
response = input("Would you like food? (Y/N):")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# Example 3
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# Example 4
for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")