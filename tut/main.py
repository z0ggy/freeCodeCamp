class Item:
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

# instantiate object of Item class
item1 = Item('Phone', 100, 5)
# print(item1.calculate_total_price(item1.price, item1.quantity))
print('total price', item1.calculate_total_price())
# print(item1.name)

item2 = Item('Laptop', 1000, 3)
# print(item2.calculate_total_price(item2.price, item2.quantity))
# print(item2.name)

item1.has_audio_jack = False
# print(item1.has_audio_jack)

# print all attributes for item1 object
for attr, value in item1.__dict__.items():
        print(attr, value)