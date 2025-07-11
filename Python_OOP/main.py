# Object Oriented Programing 
# The goal is to create a reusable, non-redundant code that can be reused for different situations if needed.

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
         return self.price * self.quantity 
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
    
item1 = Item("Phone", 100, -5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(item2.calculate_total_price())
print(item1.calculate_total_price())
