class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def print_student(self):
        print(self.id)

sa = Student(24020220, "Nguyen Tien Manh", 3.6)
sa.print_student()