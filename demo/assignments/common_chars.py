# Print common chars between 5 strings
names = ['scott','steve','tom hanks','sharne','sergy']

common = set(names[0])

for name in names:
    common = common & set(name)

print(common)


