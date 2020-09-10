nums = [-10, 10, 20, 5, -50, 1]
names = ['Java', 'javascript', 'python', 'C#', "SQL"]

for n in sorted(nums, key=abs):
    print(n, end=' ')

print("\nSorted Names ignoring case")
for n in sorted(names, key=str.upper):
    print(n, end=' ')

print("\nSorted Names by length")
for n in sorted(names, key=len):
    print(n, end=' ')