# class variables = Shared among all instances of a class
#                   Define outside the constructor
#                   Allow you to share data maong all objects created from that class


class Student:

    class_year = 2024   # this is shared by all the constructors and their elements
    num_students = 0

    def __init__(self, name, age): 
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(Student.class_year)   # accessing by the name of the class -> helps with clarity, readability

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students}")