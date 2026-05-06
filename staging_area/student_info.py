class student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa


    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students is {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The Average is {cls.total_gpa / cls.count:.2f}"
    
student1 = student("goku", 3.5)
student1 = student("vegeta", 7.5)
student1 = student("KRILLIN", 5.7)
student1 = student("gohan", 9.0)

print(student.get_count())
print(student.average_gpa())

print(student1.get_info())



