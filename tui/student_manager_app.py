from textual.app import *
from textual.widgets import *
from tui.menu_screen import MenuScreen

class StudentManagerApp(App):
    title = "QUẢN LÝ SINH VIÊN"

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane(self.title):
                yield Button("Vào menu", id="menu_button")

                yield Button("Thoát", id="exit_button")
                yield Static("Hoặc nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "exit_button":
            self.exit()
        elif button_id == "menu_button":
            self.app.push_screen(MenuScreen())

    def on_key(self, event): 
        if event.key in ("Q", "q", "escape"):
            self.exit()