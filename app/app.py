from math import e
from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Static, DataTable, Button
import openpyxl as openxyl
from textual.screen import Screen

from student_manager import StudentManager
import student_manager
import cli.cli_menu

student_manager = StudentManager()

class Menu(App):

    def compose(self) -> ComposeResult:
        # Tạo container TabbedContent
        with TabbedContent():
            # Tab Menu
            with TabPane("Menu"):
                for func in cli.cli_menu.function:
                    yield Button(cli.cli_menu.function[func], id=f"button_{str(func)}")
                yield Button("Quay lại Menu", id="back_button")
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "button_1":
            self.push_screen(AddStudentsScreen())
        elif button_id == "button_2":
            self.push_screen(ShowStudentsScreen())
        elif button_id == "back_button":
            self.pop_screen()
        elif button_id == "exit_button":
            self.exit()

    def on_key(self, event): 
        if event.key in ("Q", "escape"):
            self.exit()

class AddStudentsScreen(Screen):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Danh sách"):
                student_manager.load_from_file()
                yield Static(student_manager.show_students())
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")

class ShowStudentsScreen(Screen):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Danh sách"):
                student_manager.load_from_file()
                yield Static(student_manager.show_students())
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")