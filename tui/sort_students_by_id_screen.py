from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class SortStudentsByIDScreen(BaseScreen):
    title = "SẮP XẾP THEO MSSV"

    def compose_content(self) -> ComposeResult:
        yield Static("Tự động tải file students để làm việc. \nMặc định sắp xếp theo MSSV tăng dần.\n", id ="info")
        yield Button("Sắp xếp", id="update_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "update_button":
            out = student_manager.sort_students_by_id()
            output_widget = self.query_one("#info", Static)
            output_widget.update(out)