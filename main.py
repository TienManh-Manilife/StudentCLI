# from cli_menu import main

# if __name__ == "__main__":
#     main()



from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Static

class StudentCLI(App):
    def compose(self) -> ComposeResult:
        
        # Tạo container TabbedContent
        with TabbedContent():
            # Tab 1: Danh sách
            with TabPane("Danh sách"):
                yield Static("Danh sách sinh viên sẽ hiển thị ở đây")

            # Tab 2: Thống kê
            with TabPane("Thống kê"):
                yield Static("Thống kê dữ liệu sẽ hiển thị ở đây")

    def on_key(self, event): 
        if event.key == "q": 
            self.exit()

if __name__ == "__main__":
    StudentCLI().run()
