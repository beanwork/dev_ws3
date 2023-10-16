import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("spinbox.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()

        self.lineEdit.setText(str(min))
        self.lineEdit_2.setText(str(max))
        self.lineEdit_3.setText(str(step))

        self.horizontalSlider.setRange(min, max)
        self.horizontalSlider.setSingleStep(step)

        self.pushButton.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinbox)
        self.horizontalSlider.valueChanged.connect(self.changeSlider)

        self.pixmap = QPixmap()
        self.pixmap.load('cat.png')

        self.label_5.setPixmap(self.pixmap)
        self.label_5.resize(self.pixmap.width(), self.pixmap.height())

    def apply(self):
        min = self.lineEdit.text()
        max = self.lineEdit_2.text()
        step = self.lineEdit_3.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.horizontalSlider.setRange(int(min), int(max))
        self.horizontalSlider.setSingleStep(int(step))
    
    def changeSlider(self):
        actualValue = self.horizontalSlider.value()
        self.label_4.setText(str(actualValue))
        self.spinBox.setValue(actualValue)

    def changeSpinbox(self):
        actualValue = self.spinBox.value()
        self.label_4.setText(str(actualValue))
        self.horizontalSlider.setValue(actualValue)
    
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())