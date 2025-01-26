# Python countdown timer


# time.sleep(3)           # the program will sleep for given amount of time

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):   # count backwards // other solution: enclose range function in reversed function = reversed(range(0, my_time))
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")