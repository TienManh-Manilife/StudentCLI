from math import e
from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class ShowStudentsScreen(BaseScreen):
    title = "DANH SÁCH SINH VIÊN"

    def compose_content(self) -> ComposeResult:
        table = DataTable()
        table.add_columns("ID", "Tên", "GPA", "Năm học")
        student_manager.load_from_file()
        for student in student_manager.students:
            table.add_row(student.id, student.name, str(student.gpa), student.year)
        yield table 

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)