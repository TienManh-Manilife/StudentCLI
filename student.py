class Student:
    def __init__(self, id, name, gpa, year):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.year = year

    def __str__(self):
        return f"{self.id} - {self.name} - {self.gpa} - {self.year}"
    