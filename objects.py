class Student:
    def __init__(self, name, cl):
        self.name = name
        self.cl = cl
student = Student("Advaith", "XC")
print(student.name+" is the best student of "+student.cl)