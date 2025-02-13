
items = []
prices = []
total = 0


while True:
    item = input("Enter an item to buy (Press q to end): ")
    if item.lower() == "q":
        break
    else:
        price = float(input("What was it's cost?: "))
        amount = int(input("How many did you buy?: "))
    
        cost = amount * price    
        print(f"The total cost for {item} is: ${cost:.2f}")
        
        items.append((item, amount, cost))
        total += cost
        
print("----- Your Cart ----")

for item, amount, cost in items:
    print(f"{item} (x{amount}): ${cost:.2f}")

print(f"Your total is ${total:.2f}")

    
        






