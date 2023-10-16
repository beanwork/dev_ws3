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
        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()

        self.lineEdit.setText(str(min))
        self.lineEdit_2.setText(str(max))
        self.lineEdit_3.setText(str(step))

        self.horizontalSlider.setRange(min, max)
        self.horizontalSlider.setSingleStep(step)

        self.pushButton.clicked.connect(self.apply)
        self.pushButton_2.clicked.connect(self.savefile)
        self.pushButton_3.clicked.connect(self.openfile)

        self.spinBox.valueChanged.connect(self.changeSpinbox_and_changePixmapHeight)
        self.horizontalSlider.valueChanged.connect(self.changeSlider_and_changePixmapWidth)

        url = 'https://imageio.forbes.com/specials-images/imageserve/61b1f75e9bdd78e1c08fdd64/A-funny-labrador-dog-with-a-curiously-placed-bubble-in-its-behind-/0x0.jpg?format=jpg&crop=922,956,x0,y279,safe&width=1440'
        image = urllib.request.urlopen(url).read()

        self.pixmap = QPixmap()
        self.pixmap.loadFromData(image)
        ## resize image to fit label size
        self.pixmap = self.pixmap.scaled(self.label_5.width(), self.label_5.height())
        self.label_5.setPixmap(self.pixmap)

    def apply(self):
        min = self.lineEdit.text()
        max = self.lineEdit_2.text()
        step = self.lineEdit_3.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.horizontalSlider.setRange(int(min), int(max))
        self.horizontalSlider.setSingleStep(int(step))
    
    def changeSlider_and_changePixmapWidth(self):
        actualValue = self.horizontalSlider.value()
        self.pixmap = self.pixmap.scaled(actualValue, self.label_5.height())
        self.label_5.setPixmap(self.pixmap)

    def changeSpinbox_and_changePixmapHeight(self):
        actualValue = self.spinBox.value()
        self.pixmap = self.pixmap.scaled(self.label_width(), actualValue)
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