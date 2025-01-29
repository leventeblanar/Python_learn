# indxing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step] - spaces are not needed

credit_number = "1234-5678-9012-3456"

print(credit_number[1]) # if only 1 input - it assumes that we only want to know the "start"
print(credit_number[0:4]) # first 4 digits
print(credit_number[5:9]) # 2nd 4 digits
print(credit_number[5:]) # if we want to display the rest of the string, give only the starting point and : 
print(credit_number[-1]) # -1 means starting from the end
print(credit_number[::2]) # print every 2nd character

last_digits = credit_number[-4:] # displaying the last 4 digits using negative index
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] # negative index as steps - displays string backwards
print(credit_number)