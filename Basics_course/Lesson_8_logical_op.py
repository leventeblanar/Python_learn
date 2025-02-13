# logical operator = evaluate multiple conditions (or, and, not)
#                    or = at least on condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, bnot True)


temp = -26
is_raining = False
is_sunny = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is hot outside!")
    print("it is sunny!")
elif temp <= 0 and is_sunny:
    print("It is cold outside!")
    print("it is sunny!")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside!")
    print("it is sunny!")
elif temp >= 28 and  not is_sunny:
    print("It is hot outside!")
    print("it is cloudy!")
elif temp <= 0 and not is_sunny:
    print("It is cold outside!")
    print("it is cloudy!")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside!")
    print("it is cloudy!")