class A:
    def process(self):
        print(type(self))
        print("Method process() in A")


class B:
    def process(self):
        print("Method process() in B")


class C(A, B):
    def process(self):
        # super().process()
        A.process(self)
        B.process(self)


obj = C()
obj.process()
