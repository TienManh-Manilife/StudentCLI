from math import e
from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class SaveToFileScreen(BaseScreen):
    title = "LƯU VÀO FILE CSV"

    def compose_content(self) -> ComposeResult:
        yield Static(student_manager.save_to_file())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)