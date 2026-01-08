from textual.app import *
from textual.widgets import *
import cli.cli_menu

from tui.add_students_screen import AddStudentsScreen
from tui.classify_students_by_gpa_screen import ClassifyStudentsByGPA
from tui.delete_student_screen import DeleteStudentScreen
from tui.export_to_excel_screen import ExportToExcelScreen
from tui.find_student_screen import FindStudentScreen
from tui.import_from_excel_screen import ImportFromFileScreen
from tui.save_to_file import SaveToFileScreen
from tui.sort_students_by_gpa_screen import SortStudentsByGPAScreen
from tui.sort_students_by_id_screen import SortStudentsByIDScreen
from tui.statistical_analysis_screen import StatisticalAnalysisScreen
from tui.student_manager_app import *
from tui.base_screen import BaseScreen
from tui.show_students_screen import ShowStudentsScreen
from tui.load_from_file_screen import LoadFromFileScreen
from tui.edit_information_screen import EditInformationScreen


class MenuScreen(BaseScreen):
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
            self.app.push_screen(FindStudentScreen())
        elif button_id == "button_4":
            self.app.push_screen(DeleteStudentScreen())
        elif button_id == "button_5":
            self.app.push_screen(StatisticalAnalysisScreen())
        elif button_id == "button_6":
            self.app.push_screen(SaveToFileScreen())
        elif button_id == "button_7":
            self.app.push_screen(LoadFromFileScreen())
        elif button_id == "button_8":
            self.app.push_screen(EditInformationScreen())
        elif button_id == "button_9":
            self.app.push_screen(ExportToExcelScreen())
        elif button_id == "button_10":
            self.app.push_screen(SortStudentsByGPAScreen())
        elif button_id == "button_11":
            self.app.push_screen(SortStudentsByIDScreen())
        elif button_id == "button_12":
            self.app.push_screen(ImportFromFileScreen())
        elif button_id == "button_13":
            self.app.push_screen(ClassifyStudentsByGPA())
        else:
            super().on_button_pressed(event)
        