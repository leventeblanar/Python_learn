# In the below cases Lists, Sets and Tuples are also options to use

# 1 dimensional lists
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# alternative version

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# 2 dimensional lists

groceries = [fruits, vegetables, meats]

print(groceries[0])  
# 2d list display variations
#   [] - one quare bracket - displays the while 1d list on given index
#   [][] - displays element of given list based on indexes

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
    
    
    
    
    
# Numerical Pad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()