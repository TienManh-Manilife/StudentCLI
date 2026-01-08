from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class ExportToExcelScreen(BaseScreen):
    title = "XUẤT RA EXCEL"

    def compose_content(self) -> ComposeResult:
        yield Static("Nhập tên file Excel (mặc định students.xlsx), phải điền đuôi xlsx:")
        yield Input(placeholder="students.xlsx", id="input_filename")
        yield Static("", id="output_result")
        yield Button("Xuất ra Excel", id="update_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "update_button":
            input_widget = self.query_one("#input_filename", Input)
            file_name = input_widget.value.strip()
            if not file_name:
                file_name = "students.xlsx"
            result = student_manager.export_to_excel(file_name)
            output_widget = self.query_one("#output_result", Static)
            output_widget.update(result)
