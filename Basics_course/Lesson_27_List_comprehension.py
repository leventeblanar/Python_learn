# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [Expression for value in iterable if condition]


#doubles = []
#for x in range(1, 11):
#    doubles.append(x * 2)
#
#print(doubles)

# List comprehension shortens the above like this:

doubles = [x * 2 for x in range(1, 11)] 
triples = [x * 3 for x in range(1, 11)]
squares = [z * z for z in range(1, 11)]

fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
fruits = [fruit.upper() for fruit in fruits]


numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]



print(doubles)
print(triples)
print(squares)
print(fruits)
print(fruit_chars)
print(even_nums)


grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)