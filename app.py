from math import e
from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Static, DataTable
import openpyxl as openxyl

from student_manager import StudentManager
import student_manager

class app(App):
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
                student_manager.statistical_analysis()

    def on_key(self, event): 
        if event.key == "q" or event.key == "Q" or event.key == "escape": 
            self.exit()