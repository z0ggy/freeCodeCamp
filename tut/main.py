class Item:
    pay_rate = 0.8 # The pay rate after 10% discount
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not grather or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not grather or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_dicount(self):
         self.price = self.price * self.pay_rate

# instantiate object of Item class
item1 = Item('Phone', 100, 5)
item1.has_audio_jack = False

# print all attributes for item1 object
for attr, value in item1.__dict__.items():
        print(attr, value)
item1.apply_dicount()
print(item1.price)
item2 = Item('Laptop', 1000, 3)
item2.pay_rate = 0.7
item2.apply_dicount()
print(item2.price)
# print(Item.__dict__) # All atributes for class level
# print(item1.__dict__) # All attributes for insstance level