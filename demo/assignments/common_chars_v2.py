# Print common chars between 5 strings

common = set()  # Create empty set

for i in range(3):
    name = input("Enter name :")
    if len(common) == 0:
        common = set(name)
    else:
        common = common & set(name)

print(common)


