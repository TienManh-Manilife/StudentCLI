import re
from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class EditInformationScreen(BaseScreen):
    title = "SỬA THÔNG TIN"

    def compose_content(self) -> ComposeResult:
        yield Input(placeholder="Nhập ID sinh viên cần sửa", id="input_id")
        yield Input(placeholder="Nhập tên mới", id="input_name")
        yield Input(placeholder="Nhập GPA mới", id="input_gpa")
        yield Input(placeholder="Nhập năm học mới", id="input_year")
        yield Button("Cập nhật", id="update_button")
        yield Static("", id="output_result")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "update_button":
            id = self.query_one("#input_id", Input)
            name = self.query_one("#input_name", Input)
            gpa = self.query_one("#input_gpa", Input)
            year = self.query_one("#input_year", Input)
            output_widget = self.query_one("#output_result", Static)
            student_id = id.value.strip()
            student_name = name.value.strip()
            student_gpa = gpa.value.strip()
            student_year = year.value.strip()
            result = student_manager.edit_infomation(student_id, student_name, student_gpa, student_year)
            output_widget.update(result)