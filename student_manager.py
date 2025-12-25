import csv
from student import *

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("Danh sách trống!")
        else:
            for student in self.students:
                print(student)

    def find_student(self, student_id):
        list = [student for student in self.students 
                       if student_id == student.id or student_id == student.name]
        if list:
            for student in list:
                print(student)
        else:
            print("Sinh viên không tồn tại!")

    def delete_student(self, student_id): 
        self.students = [student for student in self.students if student.id != student_id]
        print("Đã xóa!")

    def save_to_file(self, file_name="students.csv"): 
        with open(file_name, mode="w", newline="", encoding="utf-8") as file: 
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "GPA"]) 
            for student in self.students: writer.writerow([student.id, student.name, student.gpa]) 
            print("Đã lưu dữ liệu vào file", file_name)

    def load_from_file(self, file_name="students.csv"): 
        try: 
            with open(file_name, mode="r", encoding="utf-8") as file: 
                reader = csv.DictReader(file) 
                self.students = [Student(row["ID"], row["Name"], row["GPA"]) for row in reader] 
                print("Đã tải dữ liệu từ file", file_name) 
        except FileNotFoundError: print("Chưa có file dữ liệu, bắt đầu mới.")