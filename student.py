class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def __str__(self):
        return f"{self.id} - {self.name} - {self.gpa}"
    