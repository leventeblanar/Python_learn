# Inheritance = Allows a class to ingerit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animal):  # this is good because these classes can have a shared class(Animal) and their own attributes and methods that are different form one and other
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQEEK!")

dog = Dog("Scooby")
car = Cat("Garfield")
mouse = Mouse("Mickey")

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()

dog.speak()