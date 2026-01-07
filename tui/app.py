from math import e
from textual.app import *
from textual.widgets import *
import openpyxl as openxyl
from textual.screen import Screen

from student_manager import StudentManager
import cli.cli_menu
from tui.base_screen import s_manager

class AddStudentsScreen(Screen):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Danh sách"):
                yield Static("Nhập thông tin, có thể nhập có dấu:")
                yield Input(placeholder="Nhập ID", id="input_id")
                yield Input(placeholder="Nhập tên", id="input_name")
                yield Input(placeholder="Nhập GPA hệ 4", id="input_gpa")
                yield Input(placeholder="Nhập năm học", id="input_year")
                yield Static("", id="output_result")

                yield Button("Lưu", id="save_button") 
                yield Button("Đặt lại", id="reset_button")
                yield Button("Quay lại Menu", id="back_button")
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "save_button":
            id = self.query_one("#input_id", Input).value
            name = self.query_one("#input_name", Input).value
            gpa = float(self.query_one("#input_gpa", Input).value)
            year = self.query_one("#input_year", Input).value
            student = cli.cli_menu.Student(id, name, gpa, year)
            s_manager.load_from_file()
            result = s_manager.add_student(student) + s_manager.save_to_file()
            self.query_one("#output_result", Static).update(result)

        elif button_id == "reset_button":
            self.query_one("#input_id", Input).value = ""
            self.query_one("#input_name", Input).value = ""
            self.query_one("#input_gpa", Input).value = ""
            self.query_one("#input_year", Input).value = ""

        elif button_id == "back_button":
            self.app.pop_screen()
        elif button_id == "exit_button":
            self.exit()

class ShowStudentsScreen(Screen):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Danh sách"):
                table = DataTable()
                table.add_columns("ID", "Tên", "GPA", "Năm học")
                s_manager.load_from_file()
                for student in s_manager.students:
                    table.add_row(student.id, student.name, str(student.gpa), student.year)
                yield table

                yield Button("Quay lại Menu", id="back_button")
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back_button":
            self.app.pop_screen()
        elif button_id == "exit_button":
            self.exit()