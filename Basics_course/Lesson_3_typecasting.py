# typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Levente"
age = 31
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# converting these types

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

name = bool(name)
print(name)