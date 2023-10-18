import sys
import cv2, imutils
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *


from_class = uic.loadUiType("withopencv.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.isCameraOn = False
        self.isRecStart = False
        self.recordbtn.hide()  # hide btn

        self.pixmap = QPixmap()
        self.camera = Camera(self)
        self.camera.daemon = True
        self.count = 0

        self.open_File.clicked.connect(self.openFile)
        self.camerabtn.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.recordbtn.clicked.connect(self.clickRecord)
    
    
    def openFile(self):
        file = QFileDialog.getOpenFileName(filter='Image (*.*)')

        image = cv2.imread(file[0])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        h,w,c = image.shape
        qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)
    
    def clickRecord(self):
        if self.isRecStart == False:
            self.recordbtn.setText('Rec Stop')
            self.isRecStart = True
        else:
            self.recordbtn.setText('Rec Start')
            self.isRecStart = False

    
    def clickCamera(self):
        if self.isCameraOn == False:
            self.camerabtn.setText('Camera Off')
            self.isCameraOn = True
            self.recordbtn.show()

            self.cameraStart()
        else:
            self.camerabtn.setText('Camera On')
            self.isCameraOn = False
            self.recordbtn.hide()

            self.cameraStop()
    
    def cameraStart(self):
        self.camera.running = True
        self.camera.start() # start Thread
        self.video = cv2.VideoCapture(-1)
    
    def cameraStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release
    
    def updateCamera(self):
        retval, image = self.video.read()
        if retval:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h,w,c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)
            
            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
        
        self.count += 1

class Camera(QThread):  # 매 1초마다 시그널을 보내는 쓰레드를 만듬
    update = pyqtSignal()

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = True
    
    def run(self):
        count = 0
        while self.running == True:
            self.update.emit()  # make signal
            time.sleep(0.1)
    
    def stop(self):
        self.running = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())