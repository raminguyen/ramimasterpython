""" Source: https://github.com/jimdevops19/PythonOOP/blob/main/01%20-%20Introduction%20to%20OOP/main.py"""

class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def caculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", "100", 1)

item2 = Item("Laptop", "1000", 3)

print(item1.caculate_total_price())
print(item2.caculate_total_price())

#continue at 25 seconds 

"""
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
"""

