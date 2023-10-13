import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("label.ui")[0]

class WindowClass (QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("label PyQt!")
        self.count = 0
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.reset)
        self.pushButton_3.clicked.connect(self.write)
        self.label.setText(str(self.count))

        self.lineEdit_2.textEdited.connect(self.changed)
    
    def buttonClicked(self):
        self.count += 1
        self.label.setText(str(self.count))
    
    def changed(self):
        self.lineEdit_3.setText(self.lineEdit_2.text())
    
    def write(self):
        self.label.setText(self.lineEdit.text())
        
    def reset(self):
        self.count = 0
        self.label.setText(str(self.count))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()

    sys.exit(app.exec_())