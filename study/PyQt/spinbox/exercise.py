import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

from_class = uic.loadUiType("exercise.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.height_bar.setRange(100, self.label_5.height())
        self.height_bar.setSingleStep(1)

        self.width_bar.setRange(100, self.label_5.width())
        self.width_bar.setSingleStep(1)

        self.pushButton_2.clicked.connect(self.savefile)
        self.pushButton_3.clicked.connect(self.openfile)
        self.pixmap = QPixmap()

        ## lambda를 쓰면 self.pixmap을 인자로 넣을 수 있다
        self.height_bar.valueChanged.connect(lambda : self.resize_picture(self.pixmap))
        self.width_bar.valueChanged.connect(lambda : self.resize_picture(self.pixmap))
        
    def resize_picture(self, pixmap):
        height_value = self.height_bar.value()
        width_value = self.width_bar.value()
        
        pixmap = pixmap.scaled(width_value, height_value)
        self.label_5.resize(pixmap.width(), pixmap.height())
        self.label_5.setPixmap(pixmap)

    def savefile(self):
        
        path_name = QFileDialog.getSaveFileName(self, 'save file', './')
        
        if path_name[0]:
            self.pixmap.save(path_name[0])
    
                
    def openfile(self):
        path_name = QFileDialog.getOpenFileName(self, 'open file', './')

        if path_name[0]:
            self.pixmap.load(path_name[0])
            self.pixmap = self.pixmap.scaled(self.label_5.width(), self.label_5.height(),)
            self.label_5.setPixmap(self.pixmap)                
    
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())