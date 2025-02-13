# collection = sigle "variable" used to store multiple values
#       List = [] ordered and changeable. Duplicates OK
#       Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#       Tuple = () ordered and unchangeable. Duplicates OK. FASTER


fruits = ["apple", "orange", "banana", "coconut"]
foods = {"pizza", "sushi", "hamburger", ""}
# print(dir(fruits)) - all the different methods available
# print(help(fruits)) - description of all these methods
# print(len(fruits)) - length of List
# print("apple" in fruits) - gives back boolean - shows if element is part of collection

# fruits[0] = "pineapple" - reassing values based on index position
# fruits.append("pineapple") - places new element at the end of the List
# fruits.remove("apple") - removes element
# furits.insert(0, "pineapple") - places element into a List based on given index
# fruits.sort() - sort alphabetically
# fruits.reverse() - reverese list based on index pos
# fruits.clear() - clear list completely
# fruits.index("apple") - displays index of given element
# fruits.count("coconut") - as duplicates are permitted in Lists, we can count the amount of them with .count()


...


print(fruits[1])  # number given in [] shows index of element in List, no number gives back the whole List
# 0:3 - gives elements using starting index and ending
# ::2 - gives back elements by steps


for x in fruits:
    print(x)   # this iterates throught the list
    
