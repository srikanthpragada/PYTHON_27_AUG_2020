class Product:
    def __init__(self, name, price, qoh=0):
        self.name = name
        self.price = price
        self.qoh = qoh

    def sell(self, qty):
        self.qoh -= qty

    def purchase(self, qty):
        self.qoh += qty

    def net_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - {self.price} - {self.qoh}"


class DiscountProduct(Product):
    def __init__(self, name, price, disrate):
        super().__init__(name, price)
        self.disrate = disrate

    # Override net_price
    def net_price(self):
        return self.price - (self.price * self.disrate / 100)

    def __str__(self):
        return super().__str__() + " - " + str(self.disrate)


p = Product("Abc", 10000)
print(p)
dp = DiscountProduct("Xyz", 40000, 20)
dp.purchase(10)
print(dp)

print(p.net_price())
print(dp.net_price())
