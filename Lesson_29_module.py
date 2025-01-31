# module = a file containing code you want to include in your program
#          use 'import to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# import math
import Lesson_29_module_ex
import math as m

print(m.pi)

result = Lesson_29_module_ex.pi
result1 = Lesson_29_module_ex.square(3)
result2 = Lesson_29_module_ex.cube(3) 
result3 = Lesson_29_module_ex.circumference(3) 
result4 = Lesson_29_module_ex.area(3) 


print(result1)