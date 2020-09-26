import re

f = open("contacts.txt", 'rt')
contacts = {}
for line in f.readlines():
    # look for name
    line = line.strip()  # remove leading and trailing spaces
    m = re.search("[A-Za-z ]+", line)
    if m is None:
        continue

    name = m.group().strip()
    if len(name) == 0:
        continue

        # Look for number
    m = re.search(r"\d+", line)
    if m is None:
        continue

    mobile = m.group()
    contacts[name] = mobile  # Add name and mobile to dict

for name, mobile in sorted(contacts.items()):
    print(f"{name:20} {mobile}")
