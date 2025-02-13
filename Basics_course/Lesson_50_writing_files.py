# Python writing files (.txt, .json, .csv)

import json
import csv

txt_data = 'I like pizza!'

file_path = "C:/Users/diefi/output.txt"

# employees = ["Eugene", "Squidward", "Spongebob", "Patric"]


# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }


employees = [["Name", "Age", "Job"],       # 2d collection
             ["Spongebob", 30, "Cook"],
             ["Patric", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

# with is a statement - this wraps a code to exectue but will close the file once we are done with it
# open function will return a file object - 1st parameter(file_path), 2nd is the mode
# "w" - write
# "x" - also write, if this file doesn't exist, if does exist - error
# "a" - append a file
# "r" - read

# try:                                          THIS METHOD IS TO ITERATE THROUGH A LIST AND EXPORT IT INTO A DOC
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("that file already exists")



# try:                                           THIS IS TO EXPORT A DICTIONARY INTO A JSON FILE
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"Json file '{file_path}' was created")
# except FileExistsError:
#     print("that file already exists")



try:                                    
    with open(file_path, "w", newline ="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created")
except FileExistsError:
    print("that file already exists")