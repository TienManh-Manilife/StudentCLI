from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class ImportFromFileScreen(BaseScreen):
    title = "NHẬP DỮ LIỆU TỪ FILE EXCEL"

    def compose_content(self) -> ComposeResult:
        yield Static("Load từ file students.csv, rồi thêm sinh viên vào danh sách từ file excel.\n" \
                     "Mặc định là Input.xlsx.\n" \
                    "Nếu trùng mã số thì cập nhật thông tin mới\n" \
                    "Yêu cầu có đuôi xlsx", id="info")
        yield Input(placeholder="Nhập tên file excel (mặc định input.xlsx), phải điền đuôi xlsx", id="file_input")
        yield Button("Nhập", id="update_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "update_button":
            file_input = self.query_one("#file_input", Input).value
            if not file_input:
                file_input = "input.xlsx"
            out = student_manager.import_from_excel(file_input)
            self.query_one("#info", Static).update(out)