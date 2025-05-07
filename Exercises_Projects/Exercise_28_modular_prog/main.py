from operations import Calculator

def get_number(prompt):

    while True:
            value = input(prompt).strip()
            if value.lower() == "exit":
                return "exit"
            try:
                return float(value)
            except ValueError:
                print("Invalid input value, please provide a number")

def get_operator(prompt):

    while True:
        method = input(prompt).strip()
        if method.lower() == "exit":
            return "exit"
        if method in ["+", "-", "*", "/"]:
            return method
        else:
            print("Invalid operator, please enter one of the following: +, -, *, /")


def main():

    print("**** CALCULATOR ****")
    print("Type 'exit' anytime to quit.")

    while True:
        num1 = get_number("Please select the first number: ")
        if num1 == 'exit':
            break
        num2 = get_number("Please select the second number: ")
        if num2 == 'exit':
            break
        method = get_operator("Select desired operator (+-*/): ")
        if method == 'exit':
            break

        calc = Calculator(num1, num2)

        if method == "+":
            result = calc.add()
        elif method == "-":
            result = calc.subtract()
        elif method == "*":
            result = calc.multiply()
        elif method == "/":
            result = calc.devide()
        
        print("Result: ", result)
        print("*" * 20)

if __name__ == '__main__':
    main()


