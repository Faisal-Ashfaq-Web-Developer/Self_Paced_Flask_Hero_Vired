class product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalValue(self):
        return float(self.price * self.quantity)
    
class DiscountedProduct(product):
    def __init__(self, name, price, quantity, discount):
        super().__init__(name, price, quantity)   ###/// ""super().__init__"" is used to call arguments/values from main/parent class.
        self.discount = discount
    def totalValue(self):
        discounted_price = float(self.price - (self.price*self.discount/100))
        return discounted_price * self.quantity
    
chicken = product("Chicken: ", 250, 3)
chicken_discounted = DiscountedProduct("Chicken", 250, 3, 15)
fish = product("Fish", 200, 4)
fish_discounted = DiscountedProduct("Fish: ", 200, 4, 9)

# totalValue_of_chicken = chicken.totalValue()
# totalValue_of_fish = fish.totalValue()

print("Total Value of Chicken Without Discount: ", chicken.totalValue())
print("Discounted Total Value of Chicken: ", chicken_discounted.totalValue())
print("Total Value of Fish Without Discount: ", fish.totalValue())
print("Discounted Total Value of Fish: ", fish_discounted.totalValue())



