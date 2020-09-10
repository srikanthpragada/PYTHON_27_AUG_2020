def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def set_zeroes(lst):
    for idx in range(len(lst)):
        lst[idx] = 0


a = 10
print(id(a))
zero(a)
print(a)

nums = [10, 20, 30]
set_zeroes(nums)
print(nums)
