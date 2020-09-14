class SavingsAccount:
    # constructor
    def __init__(self, acno, name, balance=0):
        # Object attributes
        self.acno = acno
        self.name = name
        self.balance = balance

    # Special method to be called to convert object to string
    def __str__(self):
        return f"{self.acno} - {self.name} - {self.balance}"

    # Methods
    def deposit(self, amount):
        self.balance += amount


a1 = SavingsAccount(1, "Jack", 10000)  # create an object
a1.deposit(20000)
print(a1)

a2 = SavingsAccount(2, "Roberts")
print(a2)
