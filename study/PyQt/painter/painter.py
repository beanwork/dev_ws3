import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import urllib.request


from_class = uic.loadUiType("paint.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)
        self.draw()

    def draw(self):
        painter = QPainter(self.label.pixmap()) # set instance of Qpainter
        
        self.pen = QPen(Qt.red, 5, Qt.SolidLine)  # change lineType and set instance of Qpen
        painter.setPen(self.pen)

        painter.drawLine(100,100,500,100)  # same format as opencv

        self.pen.setBrush(Qt.blue)
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.DashDotLine)
        painter.setPen(self.pen)

        self.line = QLine(100,200,500,200)
        painter.drawLine(self.line)

        painter.setPen(QPen(Qt.black, 20, Qt.DotLine))
        self.p1 = QPoint(100,300)
        self.p2 = QPoint(500, 300)
        painter.drawLine(self.p1, self.p2)

        painter.end

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
