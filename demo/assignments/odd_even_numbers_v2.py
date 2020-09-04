# Print even first and then odd number from the given numbers
enums = []
onums = []
while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break

    if n % 2 == 0:
        enums.append(n)
    else:
        onums.append(n)

# Print even and odd  numbers
for n in enums + onums:
    print(n)
