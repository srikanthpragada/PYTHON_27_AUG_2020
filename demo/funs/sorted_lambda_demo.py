nums = [-10, 10, 20, 5, -50, 1]
names = ['Java', 'javascript', 'python', 'C#', 'SQL', 'c++', 'c']

for n in sorted(names, key=lambda v: v[0].upper()):
    print(n, end=' ')

