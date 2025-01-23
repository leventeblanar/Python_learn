# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

print("The introduction game")
# input("What is your name?: ")

# storing inputs in variables
name = input("What is your name?: ")
print(f"Hello {name}")

age = input("How old are you?: ")

age = int(age)
age = age + 1

print("Happy birthday!")
print(f"You are {age} years old")

# this will run into an error
# as the input is a STRING by default
# in this case we have to typecast the input into an INT
# OR we could typecast the input statement itself
# age = int(input("How old are you?: "))



