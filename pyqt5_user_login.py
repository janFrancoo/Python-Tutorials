import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QtWidgets.QLabel("")
        self.id = QtWidgets.QLineEdit()
        self.pwd = QtWidgets.QLineEdit()
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButon = QtWidgets.QPushButton("Login")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.id)
        v_box.addWidget(self.pwd)
        v_box.addWidget(self.loginButon)

        self.setLayout(v_box)
        self.loginButon.clicked.connect(self.click)
        self.setWindowTitle("User Login")
        self.show()

    def click(self):
        if self.id.text() == "JanFranco" and self.pwd.text() == "12345":
            self.label.setText("Welcome!")
        else:
            self.label.setText("Wrong ID or password")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
