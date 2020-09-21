
def numbers():
    for n in range(1, 11):
        yield n

n = numbers()
print(type(n))

for v in n:
    print(v, end=' ')