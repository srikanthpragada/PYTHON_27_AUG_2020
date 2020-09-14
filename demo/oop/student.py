class Student:
    # Static attribute or Class attribute
    courses = {'Python': 10000, 'DS': 15000, 'Java': 12000}

    @staticmethod
    def get_total_fee(course):
        return Student.courses[course]

    def __init__(self, admno, name, course, feepaid=0):
        # Object attributes
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def total_fee(self):
        return Student.get_total_fee(self.course)

    def get_due(self):
        return self.total_fee() - self.feepaid

    def __str__(self):
        return f"{self.admno} - {self.name} - {self.course} - {self.feepaid}"


s = Student(1, "Abc", "Python", 3000)
s.payment(3000)
print(s.get_due())
print(s)

print(Student.get_total_fee('Python'))  # calling static method
