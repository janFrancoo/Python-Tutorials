import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkBox = QCheckBox("Python")
        self.label = QLabel("")
        self.button = QPushButton("Click!")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkBox)
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        self.button.clicked.connect(self.click)
        self.setWindowTitle("Checkbox")
        self.show()

    def click(self):
        if self.checkBox.isChecked():
            self.label.setText("Checked")
        else:
            self.label.setText("Not checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
