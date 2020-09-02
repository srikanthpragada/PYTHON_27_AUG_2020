
sum = 0
count = 0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num > 0:
        sum += num
        count += 1

print("Average of positive number :", sum // count)
