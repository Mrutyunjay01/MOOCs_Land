# -*- coding: utf-8 -*-
"""
@ author : Mrutyunjay 
"""


class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price  # these are attributes

    # a method
    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


# instantiating an object
Shirt('red', 'S', 'short-sleeveless', 15)

new_shirt = Shirt('red', 'S', 'short-sleeveless', 15)
print(new_shirt.color, new_shirt.size, new_shirt.style, new_shirt.price)

# change the price of the new shirt
new_shirt.change_price(20)
print(new_shirt.price)  # output gives 20

print(new_shirt.discount(0.2))

tshirt_collections = []
shirt_one = Shirt('orange', 'M', 'Short sleeve', 50)
shirt_two = Shirt('red', 'M', 'Long sleeve', 50)
shirt_three = Shirt('white', 'L', 'Short sleeve', 30)

tshirt_collections.append(shirt_one)
tshirt_collections.append(shirt_two)
tshirt_collections.append(shirt_three)

for i in range(len(tshirt_collections)):
    print(tshirt_collections[i].color)
