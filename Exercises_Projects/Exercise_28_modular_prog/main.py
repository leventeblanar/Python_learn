from operations import Calculator

def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input value, please provide a number")

def get_operator(prompt):

    while True:
        method = input(prompt).strip()
        if method in ["+", "-", "*", "/"]:
            return method
        else:
            print("Invalid operator, please enter one of the following: +, -, *, /")


def main():

    num1 = get_number("Please select the first number: ")
    num2 = get_number("Please select the second number: ")
    method = get_operator("Select desired operator (+-*/): ")

    calc = Calculator(num1, num2)

    if method == "+":
        result = calc.add()
    elif method == "-":
        result = calc.subtract()
    elif method == "*":
        result = calc.multiply()
    elif method == "/":
        result = calc.devide()
    
    print(result)

if __name__ == '__main__':
    main()


