class A:
    def process(self):
        print("Method process() in A")


class B(A):
    def process(self):
        print("Method process() in B")


class C(A, B):
    pass


print(C.mro())
