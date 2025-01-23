# Variable = a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the value it contains



#strings
first_name = "Levente"
food = "pizza"
email = "levente@gmail.com"

# f strings (signed by the f at the beginning)
# are used for printing texts with variables
# signed by {}

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email address is {email}")

#integer
age = 31
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#float
price = 10.99
gpa = 3.2
distance = 3.5

print(f"The price is {price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} kms")

is_student = False
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not for sale")

if is_online:
    print("The player is online")
else:
    print("The player is not online")