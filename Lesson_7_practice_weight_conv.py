# Python weight converter


weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")

if unit == "K":
    result = weight * 2.20462262
    unit = "Lbs."
    print(f"Your weight is: {round(result, 3)}{unit}")
elif unit == "L":
    result = weight * 0.45359237
    unit = "Kgs."
    print(f"Your weight is: {round(result, 3)}{unit}")
else:
    print(f"{unit} was not valid.")

