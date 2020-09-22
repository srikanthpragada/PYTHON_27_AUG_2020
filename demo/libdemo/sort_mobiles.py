# Print mobile numbers in sorted order
def ismobile(v):
    return v.isdigit() and len(v) == 10


f = open("mobiles.txt", "rt")
mobiles = []
for line in f.readlines():
    parts = line.strip().split(",")
    mobiles.extend(filter(ismobile, parts))

for number in sorted(set(mobiles)):
    print(number)

f.close()
