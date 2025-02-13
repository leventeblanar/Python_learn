# Python file detection

import os

file_path = "test.txt"

# note: we can use relative file paths (testfolder/test.txt)
# or absolute ones (C:/Users/HP/Desktop/test.txt)

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exists")