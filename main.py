from app.app import *

if __name__ == "__main__":
    i = input("Trước khi mở quản lý sinh viên, bạn muốn sử dụng giao diện nào?\n 1. Giao diện đồ họa (GUI)\n 2. Giao diện dòng lệnh (CLI)" \
    "\nLựa chọn của bạn (1 hoặc 2): ")
    if i == "2":
        from cli.cli_menu import main
        main()
    else:
        StudentApp().run()