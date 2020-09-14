class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute


p1 = Person("Bill", 20)
p1._Person__age = 30  # Access private attribute
print(p1.__dict__)

