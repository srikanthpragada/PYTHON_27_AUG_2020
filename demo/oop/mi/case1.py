class A:
    def process(self):
        print("Method process() in A")


class B:
    def task(self):
        print("Method task() in B")


class C(A, B):
    def calculate(self):
        print("Method calculate() in C")

    # Override
    def task(self):
        print("Method task() in C")


obj = C()
obj.process()
obj.task()
obj.calculate()
