class A:
    def process(self):
        print("Method process() in A")


class B(A):
    pass


class C:
    def process(self):
        print("Method process() in C")


class D(B, C):
    pass


obj = D()
obj.process()
