from unittest import case
from student_manager import StudentManager
from student import Student

function = {1: "1. Thêm sinh viên", 2: "2. Hiển thị danh sách", 3: "3. Tìm kiếm sinh viên", 4: "4. Xóa sinh viên", 5: "5. Thống kê điểm",
            6: "6. Lưu dữ liệu vào file csv", 7: "7. Tải dữ liệu từ file csv", 8: "8. Thay đổi thông tin sinh viên",
            9: "9. Xuất dữ liệu ra file excel", 10: "10. Sắp xếp sinh viên theo GPA", 11: "11. Sắp xếp sinh viên theo mã số",
            12: "12. Lấy dữ liệu từ file input.xlsx rồi thêm sinh viên vào danh sách\nNếu trùng mã số thì cập nhật thông tin mới",
            13: "13. Hiển thị xếp loại sinh viên theo GPA", 14: "14. Thoát"}
def main():
    manager = StudentManager()
    first_time = True

    while True:
        print("\n--- Student ---")
        for func in function:
            print(function[func])

        if first_time:
            first_time = False
            print(manager.load_from_file())

        choice = input("Chọn 1 trong các chức năng: ")

        if choice == "1":
            print("Nhập thông tin, có thể nhập có dấu:")
            sid = input("Nhập ID: ")
            name = input("Nhập tên: ")
            gpa = input("Nhập GPA hệ 4: ")
            year = input("Nhập năm học: ")
            student = Student(sid, name, gpa, year)
            print(manager.add_student(student))

        elif choice == "2":
            print(manager.show_students())

        elif choice == "3":
            keyword = input("Nhập ID hoặc tên: ")
            print(manager.find_student(keyword))
        elif choice == "4":
            sid = input("Nhập ID cần xóa: ")
            print(manager.delete_student(sid))

        elif choice == "5":
            print(manager.statistical_analysis())

        elif choice == "6":
            print(manager.save_to_file())

        elif choice == "7":
            print(manager.load_from_file())

        elif choice == "8":
            student_id = input("Nhập ID sinh viên cần sửa, muốn hủy hãy nhập 0: ")
            print(manager.edit_infomation(student_id))

        elif choice == "9":
            file_name = input("Nhập tên file Excel (mặc định students.xlsx), phải điền đuôi xlsx: ")
            if not file_name:
                file_name = "students.xlsx"
            print(manager.export_to_excel(file_name))
        
        elif choice == "10":
            print(manager.sort_students_by_gpa())

        elif choice == "11":
            print(manager.sort_students_by_id())
        
        elif choice == "12":
            file_name = input("Nhập tên file Excel đầu vào (mặc định input.xlsx), phải điền đuôi xlsx: ")
            if not file_name:
                file_name = "input.xlsx"
            print(manager.import_from_excel(file_name))

        elif choice == "13":
            print("Điền GPA muốn phân loại (Lấy dữ liệu lớn hơn hoặc bằng):")
            gpa = float(input("GPA: "))
            print(manager.classify_students_by_gpa(gpa))

        elif choice == "14":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

