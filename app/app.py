from math import e
from tkinter import Button
from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Static, DataTable, Button
import openpyxl as openxyl

from student_manager import StudentManager

class StudentApp(App):
    student_manager = StudentManager()

    def compose(self) -> ComposeResult:

        # Tạo container TabbedContent
        with TabbedContent():
            # Tab Menu
            with TabPane("Menu"):
                yield Button("Thêm sinh viên", id="add_student_btn")
                yield Button("Hiển thị danh sách", id="show_students_btn")
                yield Button("Tìm kiếm sinh viên", id="find_student_btn")
                yield Button("Xóa sinh viên", id="delete_student_btn")
                yield Button("Sắp xếp sinh viên", id="sort_students_btn")
                yield Button("Nhập từ file Excel", id="import_excel_btn")
                yield Button("Phân loại sinh viên", id="classify_students_btn")
                yield Button("Thống kê điểm", id="statistical_analysis_btn")

            # Tab Danh sách
            with TabPane("Danh sách"):
                table = DataTable()
                table.add_columns("ID", "Tên", "GPA", "Năm học")
                wb = openxyl.load_workbook("students.xlsx")
                sheet = wb.active
                for row in sheet.iter_rows(min_row=2, values_only=True):
                    table.add_row(*[str(cell) for cell in row])
                yield table

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "add_student_btn":
            self.push_screen("Thêm sinh viên")
        elif button_id == "show_students_btn":
            self.push_screen("Danh sách")
        elif button_id == "find_student_btn":
            self.push_screen("Tìm kiếm")
        elif button_id == "delete_student_btn":
            self.push_screen("Xóa sinh viên")
        elif button_id == "sort_students_btn":
            self.push_screen("Sắp xếp")
        elif button_id == "import_excel_btn":
            self.push_screen("Nhập từ Excel")
        elif button_id == "classify_students_btn":
            self.push_screen("Phân loại")
        elif button_id == "statistical_analysis_btn":
            self.push_screen("Thống kê")

    def on_key(self, event): 
        if event.key == "q" or event.key == "Q" or event.key == "escape": 
            self.exit()