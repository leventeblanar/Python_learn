# Python  reading files (.txt, .json, .csv)

import json
import csv

file_path = "C:/Work/test_file.txt"


# try:                                          READING A TXT file
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("The file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")



# try:                                          READING A JSON file
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("The file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")




try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])   # in case of csv files we have to read it line by line - therefore we create a for loop
        print(content)
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to read that file")