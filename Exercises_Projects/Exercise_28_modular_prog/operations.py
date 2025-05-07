class Calculator:

    def __init__(self, num1, num2, result):
        self.num1 = num1
        self.num2 = num2
        self.result = result 

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def devide(self):
        return self.num1 / self.num2