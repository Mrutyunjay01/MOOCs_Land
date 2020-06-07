# -*- coding: utf-8 -*-
"""
@ author : Mrutyunjay 
"""
class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price # these are attributes
    # a method    
    def change_price(self, new_price):
        self.price = new_price
        
    def discount(self, discount):
        return self.price * (1 - discount)

# instantiating an object    
Shirt('red', 'S', 'short-sleeveless', 15)

new_shirt = Shirt('red', 'S', 'short-sleeveless', 15)
print(new_shirt.color, new_shirt.size, new_shirt.style, new_shirt.price)

