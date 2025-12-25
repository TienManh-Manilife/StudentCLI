from student_manager import StudentManager
from student import Student

def main():
    manager = StudentManager()

    while True:
        print("\n--- Student CLI ---")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Xóa sinh viên")
        print("5. Thoát")
        print("6. Lưu dữ liệu vào file") 
        print("7. Tải dữ liệu từ file")

        manager.load_from_file()

        choice = input("Chọn 1 trong các chức năng: ")

        if choice == "1":
            print("Nhập thông tin, có thể nhập có dấu:")
            sid = input("Nhập ID: ")
            name = input("Nhập tên: ")
            gpa = input("Nhập GPA: ")
            student = Student(sid, name, gpa)
            manager.add_student(student)

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            keyword = input("Nhập ID hoặc tên: ")
            manager.find_student(keyword)

        elif choice == "4":
            sid = input("Nhập ID cần xóa: ")
            manager.delete_student(sid)

        elif choice == "5":
            print("Thoát chương trình.")
            break

        elif choice == "6":
            manager.save_to_file()

        elif choice == "7":
            manager.load_from_file()

        else:
            print("Lựa chọn không hợp lệ!")

