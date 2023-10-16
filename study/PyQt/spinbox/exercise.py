import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("spinbox.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.height.setRange(0, self.label_5.height())
        self.height.setSingleStep(1)

        self.width.setRange(0, self.label_5.width())
        self.width.setSingleStep(1)

        self.pushButton_2.clicked.connect(self.savefile)
        self.pushButton_3.clicked.connect(self.openfile)

        self.height.valueChanged.connect(self.resize)
        self.width.valueChanged.connect(self.resize)

        url = 'https://imageio.forbes.com/specials-images/imageserve/61b1f75e9bdd78e1c08fdd64/A-funny-labrador-dog-with-a-curiously-placed-bubble-in-its-behind-/0x0.jpg?format=jpg&crop=922,956,x0,y279,safe&width=1440'
        image = urllib.request.urlopen(url).read()

        self.pixmap = QPixmap()
        self.pixmap.loadFromData(image)
        ## resize image to fit label size
        self.pixmap = self.pixmap.scaled(self.label_5.width(), self.label_5.height())
        self.label_5.setPixmap(self.pixmap)

    def changeWidth(self):
        actualValue = self.width.value()
        self.pixmap = self.pixmap.scaled(actualValue, actualValue)
        self.label_5.setPixmap(self.pixmap)

    def changeHeight(self):
        actualValue = self.height.value()
        self.pixmap = self.pixmap.scaled(self.label_5.height(), actualValue)
        self.label_5.setPixmap(self.pixmap)
    
    def resize(self):
        actualValue = self.height.value()
        self.pixmap = self.pixmap.scaled(self.label_5.height(), actualValue)
        self.label_5.setPixmap(self.pixmap)

    def savefile(self):
        
        path_name = QFileDialog.getSaveFileName(self, 'save file', './')
        
        if path_name[0]:
            self.pixmap.save(path_name[0])
    
                
    def openfile(self):
        path_name = QFileDialog.getOpenFileName(self, 'open file', './')
        if path_name[0]:
            self.pixmap.load(path_name[0])
            self.pixmap = self.pixmap.scaled(self.label_5.width(), self.label_5.height())
            self.label_5.setPixmap(self.pixmap)                
    
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())