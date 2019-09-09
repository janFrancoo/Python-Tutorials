import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.textBox = QtWidgets.QLineEdit()
        self.clearButton = QtWidgets.QPushButton("Clear")
        self.printButton = QtWidgets.QPushButton("Print")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.textBox)
        v_box.addWidget(self.clearButton)
        v_box.addWidget(self.printButton)
        v_box.addStretch()

        self.setLayout(v_box)
        self.printButton.clicked.connect(self.click)
        self.clearButton.clicked.connect(self.click)
        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Clear":
            self.textBox.clear()
        elif sender.text() == "Print":
            print(self.textBox.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
