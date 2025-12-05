""" Source: https://github.com/jimdevops19/PythonOOP/blob/main/01%20-%20Introduction%20to%20OOP/main.py"""

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def caculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 1)

item2 = Item("Laptop", "1000", 3)

item1.apply_discount()

#print(item1.price)

#print(item1.caculate_total_price())
#print(item2.caculate_total_price())

#print(Item.__dict__) # All the attributes of the class
#print(item1.pay_rate)
#print(item2.pay_rate)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

"""
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
"""

