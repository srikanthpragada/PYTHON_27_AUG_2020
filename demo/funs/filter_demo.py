nums = [10, 20, 11, 45, 66, 70]


def iseven(n):
    return n % 2 == 0


print(list(filter(iseven, nums)))
