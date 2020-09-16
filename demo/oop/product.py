class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def netprice(self):
        return self.price * 1.12

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Abc", 10000)
print(p1.netprice)

p2 = Product("Abc", 10000)
p3 = Product("Xyz", 20000)

print(p1 == p2)  # p1.__eq__(p2)
# print(p3 > p2)  # p1.__gt__(p2)

products = [Product("iPhone 11", 100000),
            Product("Bose Headphones", 35000),
            Product("Nike Shoes", 8000),
            Product("Segate 1TB Harddisk", 9000)
            ]

for p in sorted(products):
    print(p)
