class A:
    def process(self):
        print("Method process() in A")


class B:
    def process(self):
        print("Method process() in B")


class C(A, B):
    def calculate(self):
        print("Method calculate() in C")


obj = C()
obj.process()
