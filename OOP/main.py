""" Source: https://github.com/jimdevops19/PythonOOP/blob/main/01%20-%20Introduction%20to%20OOP/main.py"""

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def caculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)

item2 = Item("Laptop", "1000", 3)

item1.apply_discount()

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

#for instance in Item.all:
    #print(instance.name)

"""
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
"""

