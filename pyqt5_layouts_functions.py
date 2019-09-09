import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.count = 0
        self.label = QtWidgets.QLabel("Not yet clicked on me")
        self.button = QtWidgets.QPushButton("Click Me")
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.setLayout(h_box)
        self.button.clicked.connect(self.click)
        self.show()
        
        def click(self):
            self.count += 1
            self.label.setText("{} times clicked on me".format(self.count))
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
