from math import e
from textual.app import *
from textual.widgets import *
import openpyxl as openxyl
from textual.screen import Screen
import cli.cli_menu

from tui.app import AddStudentsScreen, ShowStudentsScreen
from tui.base_screen import *

class Menu(BaseScreen):
    title = "Menu"
    is_menu = True

    def compose_content(self) -> ComposeResult:
        for func in cli.cli_menu.function:
            yield Button(cli.cli_menu.function[func], id=f"button_{str(func)}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        super().on_button_pressed(event)
        button_id = event.button.id
        if button_id == "button_1":
            self.app.push_screen(AddStudentsScreen())
        elif button_id == "button_2":
            self.app.push_screen(ShowStudentsScreen())
        