from math import e
from turtle import Screen
from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Static, DataTable, Button
import openpyxl as openxyl
from textual.screen import Screen


from student_manager import StudentManager
import student_manager

student_manager = StudentManager()

class Menu(App):

    def compose(self) -> ComposeResult:
        # Tạo container TabbedContent
        with TabbedContent():
            # Tab Menu
            with TabPane("Menu"):
                yield Button("Thêm sinh viên", id="add_student_button")
                yield Button("Hiển thị danh sách", id="show_students_button")
                yield Button("Tìm kiếm sinh viên", id="find_student_button")
                yield Button("Xóa sinh viên", id="delete_student_button")
                
                yield Button("Thoát", id="exit_button")
                yield Static("Nhấn 'Q' hoặc 'Esc' để thoát ứng dụng.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "add_student_button":
            self.push_screen(AddStudentsScreen())
        elif button_id == "show_students_button":
            self.push_screen(ShowStudentsScreen())
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