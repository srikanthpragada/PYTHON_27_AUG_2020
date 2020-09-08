def sub(n1, n2):
    return n1 - n2


def add(n1, n2):
    return n1 + n2


def mathop(n1, n2, operator):
    return operator(n1, n2)


print(mathop(10, 20, add))
print(mathop(10, 20, sub))
