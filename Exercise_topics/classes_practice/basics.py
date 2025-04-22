### This is from the Obejct Oriented programming with python - full course for Beginners

item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

class Item:
    pay_rate = 0.8 # the payrate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater then zero!"            ### assert - used to check if there is a match 
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero!"   ### to what is happening to your expectations


        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity 
    def calculate_total_price(self):
        return self.price * self.quantity 

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
print(item1.price)



# https://youtu.be/Ej_02ICOIgs?si=lOXI2-Wcb6PEJL8e&t=2537