from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class FindStudentScreen(BaseScreen):
    title = "TÌM HỌC SINH"

    def compose_content(self) -> ComposeResult:
        yield Static("Nhập ID hoặc tên sinh viên cần tìm:")
        yield Input(placeholder="Nhập id hoặc họ và tên", id="input_keyword")
        yield Static("", id="output_result")

        yield Button("Tìm kiếm", id="search_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "search_button":
            keyword = self.query_one("#input_keyword", Input).value
            result = student_manager.find_student(keyword)
            self.query_one("#output_result", Static).update(result)