from math import e
from textual.app import *
from textual.widgets import *
import openpyxl as openxyl
from textual.screen import Screen
from student_manager import StudentManager


s_manager = StudentManager()

class BaseScreen(App):
    title = "MẶC ĐỊNH"
    is_menu = False

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane(self.title):
                yield from self.compose_content()

                if not self.is_menu:
                    yield Button("Quay lại Menu", id="back_button")
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")

    def compose_content(self) -> ComposeResult:
        yield Static("Tab mặc định. Hãy ghi đè phương thức compose_content.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back_button":
            self.app.pop_screen()
        elif button_id == "exit_button":
            self.exit()

    def on_key(self, event): 
        if event.key in ("Q", "escape"):
            self.exit()