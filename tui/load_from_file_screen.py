import re
from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class LoadFromFileScreen(BaseScreen):
    title = "TẢI TỪ CSV"

    def compose_content(self) -> ComposeResult:
        yield Static("Nhập tên file cần tải (): ")
        yield Input(placeholder="Nhập tên file (Có đuôi xlsx) mặc định là students.csv", id="input_keyword")
        yield Static("Mọi chức năng làm việc với file students.csv, " \
        "nên là sau khi tải từ file khác sẽ lập tức lưu vào students.csv để làm việc.\n" \
        "=> Cần chú ý dữ liệu!", id="output_result")
        yield Button("Tải từ file", id="load_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "load_button":
            keyword = self.query_one("#input_keyword", Input).value
            if keyword == "":
                keyword = "students.csv"
            if not keyword.endswith(".csv"):
                result = "Tên file không hợp lệ! Phải có đuôi .csv"
                self.query_one("#output_result", Static).update(result)
                return
            result = student_manager.load_from_file(keyword) + student_manager.save_to_file()
            self.query_one("#output_result", Static).update(result)