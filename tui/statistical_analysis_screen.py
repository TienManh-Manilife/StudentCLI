from turtle import st
from textual.app import *
from textual.widgets import *

from total_instances import student_manager
from tui.base_screen import *

class StatisticalAnalysisScreen(BaseScreen):
    title = "THỐNG KÊ ĐIỂM"

    def compose_content(self) -> ComposeResult:
        yield Static(student_manager.statistical_analysis())