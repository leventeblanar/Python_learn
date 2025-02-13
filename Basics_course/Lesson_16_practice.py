# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower == "q": # .lower to make the input lowercase (Q would not quit the while loop)
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        foods.append(food)
        prices.append(price)
        
print("----- YOUR CART -----")

for food in foods:
    print(food)
    
for price in prices: 
    total += price
    
print(f"Your total: ${total}")