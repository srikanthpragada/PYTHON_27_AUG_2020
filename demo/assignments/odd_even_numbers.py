nums = []
while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break
    nums.append(n)

# Print even numbers
for n in nums:
    if n % 2 == 0:
        print(n)
# Print Odd numbers
for n in nums:
    if n % 2 != 0:
        print(n)
