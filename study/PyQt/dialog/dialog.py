import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("dialog.ui")[0]

class WindowClass (QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dialog")

        self.pushButton.clicked.connect(self.inputName)
        self.pushButton_2.clicked.connect(self.inputseason)
        self.pushButton_3.clicked.connect(self.inputcolor)
        self.pushButton_4.clicked.connect(self.changefont)
        self.pushButton_5.clicked.connect(self.openfile)
        # self.lineEdit.returnPressed.connect(self.inputnumber)
        self.lineEdit.returnPressed.connect(self.question)

    def inputName(self):
        text, ok = QInputDialog.getText(self, 'QinDialog - Name', 'User name:')

        if text and ok:
            self.textEdit.append(text)
    
    def inputseason(self):
        items = ['Spring', 'Summer', 'Fall', 'Winter']

        item, ok = QInputDialog.getItem(self, 'season', 'season',
                                         items, 0 ,False)
        if ok and item:
            self.textEdit.append(item)
    
    def inputcolor(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.textEdit.append("color")
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.End)  ## role is deselect All
    
    def changefont(self):
        font, ok = QFontDialog.getFont()

        if font and ok:
            info = QFontInfo(font)
            self.textEdit.append(info.family() + info.styleName())
            self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.End)
    
    def openfile(self):
        name = QFileDialog.getOpenFileName(self, 'open file', './')

        if name[0]:
            with open(name[0], 'r') as file:
                data = file.read()
                self.textEdit.append(data)
    
    def inputnumber(self):
        text = self.lineEdit.text()

        if text.isdigit():
            self.textEdit.setText(text)
        else:
            QMessageBox.warning(self, 'QMessagebox - setText', 'Please enter only numbers')
            self.lineEdit.clear()

    def question(self):
        text = self.lineEdit.text()

        if text.isdigit():
            self.textEdit.setText(text)
        
        else:
            retval = QMessageBox.question(self, 'QMessageBox - question', 'Are you sure Print?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if retval == QMessageBox.Yes:
                self.textEdit.setText(text)
            else:
                self.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())