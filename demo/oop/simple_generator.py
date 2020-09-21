def three():
    for v in range(3):
        yield v


g = three()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
