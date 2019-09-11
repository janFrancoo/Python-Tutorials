import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.infoLabel = QLabel("What is your fav lang?")
        self.radioButton = QRadioButton("C")
        self.radioButton2 = QRadioButton("Java")
        self.radioButton3 = QRadioButton("Python")
        self.radioButton4 = QRadioButton("MATLAB")
        self.label = QLabel("")
        self.button = QPushButton("Click!")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radioButton)
        v_box.addWidget(self.radioButton2)
        v_box.addWidget(self.radioButton3)
        v_box.addWidget(self.radioButton4)
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        self.button.clicked.connect(lambda: self.click(self.radioButton.isChecked(),
                                                             self.radioButton2.isChecked(),
                                                             self.radioButton3.isChecked(),
                                                             self.radioButton4.isChecked(),
                                                             self.label))
        self.setWindowTitle("Checkbox")
        self.show()

    def click(self, c, java, python, matlab, label):
        if c:
            label.setText("C")
        if java:
            label.setText("Java")
        if python:
            label.setText("Python")
        if matlab:
            label.setText("MATLAB")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
