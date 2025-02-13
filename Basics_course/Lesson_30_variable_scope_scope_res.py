# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local - the variable declaration is in the function and that variable can only be used by the function
# Enclosed - function in a function - if variable is in enclosed function - use local one, if the variable is in the main function above the enclosed on, use enclosed variable
# Global - variable is outside of any finction - any function can use it


from math import e

def func1():
    print(x)

def func2():
    b = 3
    print(b)
    

x = 1

func1()
func2()

e = 3