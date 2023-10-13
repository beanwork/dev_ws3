import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("Test.ui")[0]

class WindowClass (QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test PyQt!")
        
        self.pushButton.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)
        self.pushButton_3.clicked.connect(self.button3_Clicked)

        self.checkBox.clicked.connect(self.check1_Clicked)
        self.checkBox_2.clicked.connect(self.check2_Clicked)
        self.checkBox_3.clicked.connect(self.check3_Clicked)
        self.checkBox_4.clicked.connect(self.check4_Clicked)
    
    def check1_Clicked(self):
        if (self.checkBox.isChecked()):
            self.textEdit.setText("checkbox 1 checked")
            self.checkBox_5.setChecked(True)
        else:
            self.textEdit.setText("checkbox1 unchecked")
            self.checkBox_5.setChecked(False)

    def check2_Clicked(self):
        if (self.checkBox_2.isChecked()):
            self.textEdit.setText("checkbox 2 checked")
            self.checkBox_6.setChecked(True)
        else:
            self.textEdit.setText("checkbox2 unchecked")
            self.checkBox_6.setChecked(False)

    def check3_Clicked(self):
        if (self.checkBox_3.isChecked()):
            self.textEdit.setText("checkbox 3 checked")
            self.checkBox_7.setChecked(True)
        else:
            self.textEdit.setText("checkbox3 unchecked")
            self.checkBox_7.setChecked(False)
        
    def check4_Clicked(self):
        if (self.checkBox_4.isChecked()):
            self.textEdit.setText("checkbox 4 checked")
            self.checkBox_8.setChecked(True)
        else:
            self.textEdit.setText("checkbox4 unchecked")
            self.checkBox_8.setChecked(False)
    
    # def radio_Clicked(self):
    #     if self.radio_1.isChecked():
    #         self.textEdit.setText("radio 1")
    #     elif self.radio_2.isChecked():
    #         self.textEdit.setText("radio 2")
    #     elif self.radio_3.isChecked():
    #         self.textEdit.setText("radio 3")
    #     else:
    #         self.textEdit.setText("unknown")

    # def radio1_Clicked(self):
    #     self.textEdit.setText("radio 1")

    # def radio2_Clicked(self):
    #     self.textEdit.setText("radio 2")

    # def radio3_Clicked(self):
    #     self.textEdit.setText("radio 3")

    def button1_Clicked(self):
        self.textEdit.setText("Button1")
        self.radio_1.setChecked(True)

    def button2_Clicked(self):
        self.textEdit.setText("Button2")
        self.radio_2.setChecked(True)

    def button3_Clicked(self):
        self.textEdit.setText("Button 3")
        self.radio_3.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()

    sys.exit(app.exec_())