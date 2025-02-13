# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


numbers = (1, 2, 3, 4, 5)

for number in (numbers):
    print(number, end=" ")


fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)



my_dictionary = {"A":1, "B": 2, "C": 3}

for key, value in my_dictionary.values():
    print(f"{key} = {value}")

