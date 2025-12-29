from student_manager import StudentManager
from student import Student

def main():
    manager = StudentManager()
    first_time = True

    while True:
        print("\n--- Student ---")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Xóa sinh viên")
        print("5. Thoát")
        print("6. Lưu dữ liệu vào file") 
        print("7. Tải dữ liệu từ file")
        print("8. Thay đổi thông tin sinh viên")
        print("9. Xuất dữ liệu ra file Excel")
        print("10. Sắp xếp sinh viên theo GPA")
        print("11. Sắp xếp sinh viên theo mã số")
        print("12. Lấy dữ liệu từ file input.xlsx rồi thêm sinh viên vào danh sách\nNếu trùng mã số thì cập nhật thông tin mới")
        print("13. Hiển thị xếp loại sinh viên theo GPA")
        print("14. Thống kê điểm")

        if first_time:
            first_time = False
            manager.load_from_file()

        choice = input("Chọn 1 trong các chức năng: ")

        if choice == "1":
            print("Nhập thông tin, có thể nhập có dấu:")
            sid = input("Nhập ID: ")
            name = input("Nhập tên: ")
            gpa = input("Nhập GPA hệ 4: ")
            year = input("Nhập năm học: ")
            student = Student(sid, name, gpa, year)
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

        elif choice == "8":
            student_id = input("Nhập ID sinh viên cần sửa, muốn hủy hãy nhập 0: ")
            manager.edit_infomation(student_id)

        elif choice == "9":
            file_name = input("Nhập tên file Excel (mặc định students.xlsx), phải điền đuôi xlsx: ")
            if not file_name:
                file_name = "students.xlsx"
            manager.export_to_excel(file_name)
        
        elif choice == "10":
            manager.sort_students_by_gpa()

        elif choice == "11":
            manager.sort_students_by_id()
        
        elif choice == "12":
            file_name = input("Nhập tên file Excel đầu vào (mặc định input.xlsx), phải điền đuôi xlsx: ")
            if not file_name:
                file_name = "input.xlsx"
            manager.import_from_excel(file_name)

        elif choice == "13":
            print("Điền GPA muốn phân loại (Lấy dữ liệu lớn hơn hoặc bằng):")
            gpa = float(input("GPA: "))
            manager.classify_students_by_gpa(gpa)

        elif choice == "14":
            manager.statistical_analysis()

        else:
            print("Lựa chọn không hợp lệ!")

