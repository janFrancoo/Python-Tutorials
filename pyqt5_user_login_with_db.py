import sys
import pyodbc
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect()

    def connect(self):
        self.con = pyodbc.connect("DRIVER={SQL Server};"
                             "SERVER=localhost;"
                             "DATABASE=forPython;"
                             "UID=janfranco;"
                             "PWD=123456789;"
                             "Trusted_Connection=yes;")
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE TABLE login (username varchar(max), passwd varchar(max))')
        self.con.commit()
        self.label.setText("Connected")

    def register_user(self, new_id, new_pwd):
        self.cursor.execute('INSERT INTO login ([username], [passwd]) VALUES (?, ?)', new_id, new_pwd)
        self.con.commit()
        self.label.setText("Registered successfully!")

    def check_user(self, id, pwd):
        self.cursor.execute("SELECT * FROM login WHERE username = ? AND passwd = ?", id, pwd)
        ctrl = self.cursor.fetchall()

        if len(ctrl) == 0:
            return False
        else:
            return True

    def init_ui(self):
        self.label = QtWidgets.QLabel("")
        self.id = QtWidgets.QLineEdit()
        self.pwd = QtWidgets.QLineEdit()
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton = QtWidgets.QPushButton("Login")
        self.regButton = QtWidgets.QPushButton("Register")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.id)
        v_box.addWidget(self.pwd)
        v_box.addWidget(self.loginButton)
        v_box.addWidget(self.kayitButon)

        self.setLayout(v_box)
        self.loginButton.clicked.connect(self.click)
        self.kayitButton.clicked.connect(self.click)
        self.setWindowTitle("User Login")
        self.show()

    def click(self):
        sender = self.sender()
        if sender.text() == "Login":
            if self.check_user(self.id.text(), self.pwd.text()):
                self.label.setText("Welcome!")
            else:
                self.label.setText("Wrong ID or Pwd")
        elif sender.text() == "Register":
            self.register_user(self.id.text(), self.pwd.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
