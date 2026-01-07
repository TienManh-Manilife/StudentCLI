from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class DeleteStudent(BaseScreen):
    title = "XÓA HỌC SINH"

    def compose_content(self) -> ComposeResult:
        yield Static("Nhập ID sinh viên cần xóa: ")
        yield Input(placeholder="Nhập id", id="input_keyword")
        yield Static("", id="output_result")

        yield Button("Tìm kiếm và xóa", id="search_and_delete_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "search_and_delete_button":
            keyword = self.query_one("#input_keyword", Input).value
            result = student_manager.delete_student(keyword)
            self.query_one("#output_result", Static).update(result)