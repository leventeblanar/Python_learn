# default arguments = a default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. dEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05))

# if there is a given value even though there is a default, it overwrites the default one


import time

def count(end, start=0):  # switched places because of the logical positioning
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

count(10)  # the problem is that default arguments have to be positioned at the end of the line as the input values would be overwriting them