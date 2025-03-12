# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
mylist2 = [2, 5, 7, 3, 5, 11, 5, 33, 60,]
print(mylist)

# mylist2 = [5, True, "apple", "apple"]

# item = mylist[0]
# print(item)

# iterate through list
for i in mylist:
    print(i)

# conditions to check in list
if "banana" in mylist:
    print('yes')
else:
    print('no')

# length of list (number of elements)
print(len(mylist))

# add to lsit
mylist.append("lemon")

# add at specific position
mylist.insert(1, "blueberry")
print(mylist)

# remove last one
item = mylist.pop()
print(item)
print(mylist)

# remove at specific loc
item = mylist.remove("cherry")

# clear complete list
# item = mylist.clear()
# print(mylist)

# reverse list
item = mylist.reverse()
print(mylist)

# sort list
new_list = sorted(mylist2)
print(mylist2)
print(new_list)

mylist3 = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]

new_list2 = mylist + mylist2
print(new_list2)


# separating lists
mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist4[1:5] #start index - end index - if not specified it goes all the way to that direction
print(a)

#step operator
b = mylist4[::2] # displays every second item
print(b)

#reverse list
c = mylist4[::-1]
print(c)

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org [:] #eithout slicing both of the list will be modified
list_cpy.append("lemon")
print(list_cpy)
print(list_org)


mylist6 = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist6]

print(mylist6)
print(b)