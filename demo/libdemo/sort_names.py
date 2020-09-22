# Print names in sorted order

f = open("names.txt", "rt")

for line in sorted(f.readlines()):
    print(line, end='')

f.close()
