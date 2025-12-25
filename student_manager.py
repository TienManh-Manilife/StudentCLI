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
        has_in_list = [student for student in self.students if student_id == student.id]
        if has_in_list:
            for student in has_in_list:
                print(student)

    def delete_student(self, student_id): 
        self.students = [s for s in self.students if s.id != student_id]
        print("Đã xóa!")