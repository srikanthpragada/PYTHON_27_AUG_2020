import re


# Print valid mobile numbers in sorted order
def ismobile(v):
    return len(v) == 10


f = open("phones.txt", "rt")
mobiles = []
for line in f.readlines():
    # parts = re.split(r"\D+", line)
    parts = re.findall(r"\d+", line)
    mobiles.extend(filter(ismobile, parts))

for number in sorted(set(mobiles)):
    print(number)

f.close()
