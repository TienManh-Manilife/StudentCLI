from math import e
from textual.app import *
from textual.widgets import *
import openpyxl as openxyl
from textual.screen import Screen
import cli.cli_menu

from tui.add_students_screen import AddStudentsScreen
from tui.find_student_screen import FindStudent
from tui.student_manager_app import *
from tui.base_screen import BaseScreen
from tui.show_students_screen import ShowStudentsScreen


class Menu(BaseScreen):
    title = "MENU"
    is_menu = True

    def compose_content(self) -> ComposeResult:
        for func in cli.cli_menu.function:
            yield Button(cli.cli_menu.function[func], id=f"button_{str(func)}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "button_1":
            self.app.push_screen(AddStudentsScreen())
        elif button_id == "button_2":
            self.app.push_screen(ShowStudentsScreen())
        elif button_id == "button_3":
            self.app.push_screen(FindStudent())
        else:
            super().on_button_pressed(event)
        