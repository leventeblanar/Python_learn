# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 11):   # some people call x as counter in code as well, (1, 11) - 1st: where begin, 2nd: where stop, 3rd: steps to take in each iteration
    print(x)
    
print("Happy New Year!")


credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else: 
        print(x)