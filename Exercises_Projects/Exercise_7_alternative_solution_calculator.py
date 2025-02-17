import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import operator

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title and size
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Main layout to contain all widgets
        main_layout = QVBoxLayout()

        # Create an input field for displaying the current expression or result
        self.input_field = QLineEdit()
        self.input_field.setAlignment(Qt.AlignRight)  # Align text to the right for calculator-style display
        self.input_field.setReadOnly(True)  # Make it read-only so users cannot type directly
        self.input_field.setStyleSheet("font-size: 24px;")  # Set font size for better readability
        main_layout.addWidget(self.input_field)  # Add the input field to the main layout

        # Layout to arrange the calculator buttons
        buttons_layout = QGridLayout()

        # Define button labels and their positions in the grid
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),  # Row 0
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),  # Row 1
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),  # Row 2
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),  # Row 3
            ('=', 4, 0, 1, 4)  # Row 4 (span 4 columns)
        ]

        # Create and configure each button
        for label, row, col, *span in buttons:
            button = QPushButton(label)  # Create a button with the specified label
            button.setStyleSheet("font-size: 18px; padding: 10px;")  # Set button style
            button.clicked.connect(self.on_button_click)  # Connect button click to handler
            if span:
                buttons_layout.addWidget(button, row, col, *span)  # Add button with span if specified
            else:
                buttons_layout.addWidget(button, row, col)  # Add button without span

        main_layout.addLayout(buttons_layout)  # Add the buttons layout to the main layout
        self.setLayout(main_layout)  # Set the main layout for the window

        # Define operations and their corresponding functions
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        self.current_expression = ""  # Variable to store the current expression
        self.result_displayed = False  # Track whether the result is currently displayed

    def on_button_click(self):
        # Get the button that was clicked
        sender = self.sender()
        label = sender.text()  # Get the label of the clicked button

        if label == "C":
            # Clear the current expression and reset the input field
            self.current_expression = ""
            self.input_field.setText("")
            self.result_displayed = False
        elif label == "=":
            # Calculate the result when '=' is pressed
            self.calculate_result()
        else:
            # Handle other button clicks (numbers, operators, etc.)
            if self.result_displayed:
                if label in self.operations:
                    # If an operator is pressed after result, allow continuation
                    self.result_displayed = False
                else:
                    # If a number or '.' is pressed, start a new expression
                    self.current_expression = ""
                    self.result_displayed = False
            self.current_expression += label  # Append the label to the current expression
            self.input_field.setText(self.current_expression)  # Update the input field

    def calculate_result(self):
        try:
            # Safely evaluate the current expression
            result = self.evaluate_expression(self.current_expression)
            self.input_field.setText(str(result))  # Display the result
            self.current_expression = str(result)  # Update the current expression with the result
            self.result_displayed = True  # Indicate that the result is displayed
        except Exception as e:
            # Handle errors (e.g., invalid expressions)
            self.input_field.setText("Error")  # Display error message
            self.current_expression = ""  # Reset the expression
            self.result_displayed = False

    def evaluate_expression(self, expression):
        # Custom method to parse and evaluate simple math expressions
        stack = []  # Stack to store numbers and intermediate results
        num = ""  # Variable to build numbers from characters
        op = None  # Variable to store the current operator

        for char in expression:
            if char.isdigit() or char == ".":
                # Build a number if the character is a digit or a decimal point
                num += char
            elif char in self.operations:
                # Handle operators
                if num:
                    stack.append(float(num))  # Push the current number to the stack
                    num = ""  # Reset the number
                if len(stack) >= 2 and op:
                    # Perform the previous operation if two numbers are in the stack
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(self.operations[op](a, b))  # Push the result back to the stack
                op = char  # Update the current operator

        if num:
            stack.append(float(num))  # Push the last number to the stack
        if len(stack) == 2 and op:
            # Perform the final operation
            b = stack.pop()
            a = stack.pop()
            return self.operations[op](a, b)  # Return the result
        return stack[0] if stack else 0  # Return the remaining number or 0 if the stack is empty

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    calculator = Calculator()  # Instantiate the Calculator class
    calculator.show()  # Show the calculator window
    sys.exit(app.exec_())  # Execute the application event loop