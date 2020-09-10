g = 100  # Global variables


def fun1():
    l = 10
    global g
    g = g + 1
    print('fun1()')
    print(g, l)


def outer_function():
    print("Outer")
    a = 10  # Enclosing variable

    def inner_function():
        print("Inner")
        nonlocal a
        a = 0
        b = 20       # Local variable
        print(a, b)

    inner_function()
    print(a)

# fun1()
# print(g)
outer_function()
