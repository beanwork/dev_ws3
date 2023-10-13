import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("textbrowser.ui")[0]

class WindowClass (QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TextBrowser")

        self.pushButton.clicked.connect(self.addText)
        self.pushButton_2.clicked.connect(self.clearText)
        self.pushButton_3.clicked.connect(lambda: self.setFont("Ubuntu"))
        self.pushButton_4.clicked.connect(lambda: self.setFont("NanumGothic"))
        self.pushButton_5.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.pushButton_6.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.pushButton_7.clicked.connect(lambda: self.setTextColor(0, 0, 255))
        self.pushButton_8.clicked.connect(self.Fontsize)

    def addText(self):
        input = self.textEdit_2.toPlainText()
        self.textEdit_2.clear()
        self.textEdit.append(input)    
    
    def clearText(self):
        self.textEdit_2.clear()
        self.textEdit.clear()

    def setFont(self, fontName):
        font = QFont(fontName, 11)
        self.textEdit.setFont(font)
    
    def setTextColor(self, r, g, b):
        color = QColor(r, g, b)
        self.textEdit.selectAll()
        self.textEdit.setTextColor(color)
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
    
    def Fontsize(self):
        size = int(self.textEdit_3.toPlainText())
        self.textEdit.selectAll()
        self.textEdit.setFontPointSize(size)
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())