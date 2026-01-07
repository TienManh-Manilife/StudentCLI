from math import e
from textual.app import *
from textual.widgets import *
from tui.base_screen import *

import cli.cli_menu
from total_instances import student_manager

class AddStudentsScreen(BaseScreen):
    title = "THÊM SINH VIÊN"

    def compose_content(self) -> ComposeResult:
        yield Static("Nhập thông tin, có thể nhập có dấu:")
        yield Input(placeholder="Nhập ID", id="input_id")
        yield Input(placeholder="Nhập tên", id="input_name")
        yield Input(placeholder="Nhập GPA hệ 4", id="input_gpa")
        yield Input(placeholder="Nhập năm học", id="input_year")
        yield Static("", id="output_result")

        yield Button("Lưu", id="save_button") 
        yield Button("Đặt lại", id="reset_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "save_button":
            id = self.query_one("#input_id", Input).value
            name = self.query_one("#input_name", Input).value
            gpa = float(self.query_one("#input_gpa", Input).value)
            year = self.query_one("#input_year", Input).value
            student = cli.cli_menu.Student(id, name, gpa, year)
            student_manager.load_from_file()
            result = student_manager.add_student(student) + student_manager.save_to_file()
            self.query_one("#output_result", Static).update(result)

        elif button_id == "reset_button":
            self.query_one("#input_id", Input).value = ""
            self.query_one("#input_name", Input).value = ""
            self.query_one("#input_gpa", Input).value = ""
            self.query_one("#input_year", Input).value = ""

        else :
            super().on_button_pressed(event)