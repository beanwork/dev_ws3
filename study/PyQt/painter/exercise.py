import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, uic
from PyQt5.QtCore import *
import urllib.request


from_class = uic.loadUiType("exercise.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

    def mouseMoveEvent(self, event):
        txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        self.label_3.setText(txt)

    def mousePressEvent(self, event): 
        if event.buttons() & Qt.LeftButton:
            self.label.setText("left")

        if event.buttons() & Qt.MidButton:  # wheel button
            self.label.setText("middle")

        if event.buttons() & Qt.RightButton:
            self.label.setText("right")
    
    def wheelEvent(self, event):
        txt = " x={0},y={1}".format(event.angleDelta().x(), event.angleDelta().y())
        self.label_2.setText(txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())