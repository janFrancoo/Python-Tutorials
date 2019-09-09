import sys
from PyQt5 import QtWidgets, QtGui

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    
    button = QtWidgets.QPushButton(window)
    button.setText("Click Me")
    button.move(150, 350)
    
    label_1 = QtWidgets.QLabel(window)
    label_1.setText("This a label")
    label_1.move(175, 40)
    
    label_2 = QtWidgets.QLabel(window)
    label_2.setPixmap(QtGui.QPixmap("python.png"))
    label_2.move(50, 50)
    
    window.setWindowTitle("JFBlog")
    window.setGeometry(100, 100, 400, 400)  # 100 - 100 location, 500 - 500 size
    window.show()
    sys.exit(app.exec_())
    
main_window()
