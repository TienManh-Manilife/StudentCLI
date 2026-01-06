from math import e
from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Static, DataTable
import openpyxl as openxyl

from student_manager import StudentManager
import student_manager

class StudentApp(App):
    student_manager = StudentManager()

    def compose(self) -> ComposeResult:

        # Tạo container TabbedContent
        with TabbedContent():
            # Tab Menu
            with TabPane("Menu"):
                yield Static("Chức năng sinh viên sẽ hiển thị ở đây")

            # Tab Danh sách
            with TabPane("Danh sách"):
                table = DataTable()
                table.add_columns("ID", "Tên", "GPA", "Năm học")

                wb = openxyl.load_workbook("students.xlsx")
                sheet = wb.active
                for row in sheet.iter_rows(min_row=2, values_only=True):
                    table.add_row(*[str(cell) for cell in row])
                yield table

            # Tab Thống kê
            with TabPane("Thống kê"):
                stats = self.student_manager.statistical_analysis() 
                yield Static(stats)

            # Tab Thêm sinh viên
            with TabPane("Thêm sinh viên"):
                yield Static("Form thêm sinh viên sẽ hiển thị ở đây")

            # Tab Tìm kiếm
            with TabPane("Tìm kiếm"):  
                yield Static("Form tìm kiếm sinh viên sẽ hiển thị ở đây")

            # Tab Xóa sinh viên
            with TabPane("Xóa sinh viên"):
                yield Static("Form xóa sinh viên sẽ hiển thị ở đây")

            # Tab Sắp xếp
            with TabPane("Sắp xếp"):
                yield Static("Chức năng sắp xếp sinh viên sẽ hiển thị ở đây")

            # Tab Nhập từ Excel
            with TabPane("Nhập từ Excel"):
                yield Static("Chức năng nhập sinh viên từ file Excel sẽ hiển thị ở đây")

            # Tab Phân loại
            with TabPane("Phân loại"):
                yield Static("Chức năng phân loại sinh viên sẽ hiển thị ở đây")

            # Tab kết quả
            with TabPane("Kết quả"):
                yield Static("Kết quả sẽ hiển thị ở đây")

    def on_key(self, event): 
        if event.key == "q" or event.key == "Q" or event.key == "escape": 
            self.exit()