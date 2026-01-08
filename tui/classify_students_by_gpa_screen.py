from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class ClassifyStudentsByGPA(BaseScreen):
    title = "PHÂN LOẠI SINH VIÊN THEO GPA"

    def compose_content(self) -> ComposeResult:
        yield Static("Tự động load từ file students.csv\n Điền GPA muốn phân loại vào\n" \
        "Sẽ hiển thị sinh viên có GPA >= GPA nhập vào")
        yield Input(placeholder="Nhập gpa", id="file_input")
        yield Button("Nhập", id="update_button")
        yield Static("", id="info")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "update_button":
            input = self.query_one("#file_input", Input).value
            if not input:
                out = "Vui lòng nhập GPA hợp lệ!"
                self.query_one("#info", Static).update(out)
                return
            out = student_manager.classify_students_by_gpa(float(input))
            self.query_one("#info", Static).update(out)