# Take price and display net price after discount

price = float(input("Enter price :"))

if price > 10000:
    discount = price * 0.30
elif price > 5000:
    discount = price * 0.20
else:
    discount = price * 0.10

print(f"Base Price  : {price:6.0f}")
print(f" - Discount : {discount:6.0f}")
print(f"              {'-' * 6}")
print(f"Net price   : {price - discount:6.0f}")

