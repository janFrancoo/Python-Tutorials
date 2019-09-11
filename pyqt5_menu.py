import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        menu_bar = self.menuBar()
        file = menu_bar.addMenu("File")
        edit = menu_bar.addMenu("Edit")

        open_file = QAction("Open File", self)
        open_file.setShortcut("Ctrl + O")

        save_file = QAction("Save File", self)
        save_file.setShortcut("Ctrl + S")

        exit = QAction("Exit", self)
        exit.setShortcut("Ctrl + Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(exit)

        search_and_change = edit.addMenu("Search and Change")
        search = QAction("Search", self)
        change = QAction("Change", self)

        search_and_change.addAction(search)
        search_and_change.addAction(change)

        clear = QAction("Clear", self)
        edit.addAction(clear)

        exit.triggered.connect(lambda: qApp.exit())
        file.triggered.connect(self.response)

        self.setWindowTitle("Menu")
        self.show()

    def response(self, action):
        if action.text() == "Open File":
            print("User clicked open file")
        elif action.text() == "Save File":
            print("User clicked save file")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())
