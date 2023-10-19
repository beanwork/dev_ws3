import sys
import cv2, imutils
import datetime
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *

from_class = uic.loadUiType("cameraApp.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.isCameraOn = False
        self.isRecStart = False

        '--------hide btn--------'
        self.recordbtn.hide()  
        self.capturebtn.hide()
        self.videobtn.hide()

        self.pixmap = QPixmap()

        '----------thread-------------'
        self.cam_thread = SendSignal(self)
        self.cam_thread.daemon = True

        self.rec_thread = SendSignal(self)
        self.rec_thread.daemon = True

        self.vid_thread = SendSignal(self)
        self.vid_thread.daemon = True

        '-----------openfile-----------'
        self.open_File.clicked.connect(self.openFile)
        
        '-----------camera-------------'
        self.camerabtn.clicked.connect(self.clickCamera)
        self.cam_thread.update.connect(self.updateCamera)

        '-----------record-------------'
        self.recordbtn.clicked.connect(self.clickRecord)
        self.rec_thread.update.connect(self.updateRecord)

        '-----------capture------------'
        self.capturebtn.clicked.connect(self.capture)

        '-----------video---------'
        self.vid_thread.update.connect(self.updateVideo)
        self.videobtn.clicked.connect(self.clickVideo)
    
    
    def openFile(self):

        file_name = QFileDialog.getOpenFileName(self, 'open file', './')

        if file_name[0].split('.')[1] in ['avi', 'mp4']: 
            self.video = cv2.VideoCapture(file_name[0])
            self.videoStart()

        else:
            image = cv2.imread(file_name[0])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h,w,c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            
            self.label.setPixmap(self.pixmap)
    

    '-----------------------RECORD---------------------'
    def clickRecord(self):
        if self.isRecStart == False:
            self.recordbtn.setText('Rec Stop')
            self.isRecStart = True

            self.recordingStart()

        else:
            self.recordbtn.setText('Rec Start')
            self.isRecStart = False

            self.recordingStop()
    
    def recordingStart(self):
        self.rec_thread.running = True
        self.rec_thread.start()

        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = self.now + '.avi'
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        w = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.writer = cv2.VideoWriter(filename, self.fourcc, 20.0, (w,h))
    
    def recordingStop(self):
        self.rec_thread.running = False

        if self.isRecStart == True:
            self.writer.release()

    def updateRecord(self):
        retval, image = self.camera.read()
        if retval:
            self.writer.write(image)


    '-----------------------CAMERA---------------------'
    def clickCamera(self):
        if self.isCameraOn == False:
            self.camerabtn.setText('Camera Off')
            self.isCameraOn = True
            self.recordbtn.show()
            self.capturebtn.show()

            self.cameraStart()
        else:
            self.camerabtn.setText('Camera On')
            self.isCameraOn = False
            self.recordbtn.hide()
            self.capturebtn.hide()

            self.cameraStop()
            self.recordingStop()  # if camera off, record video
    
    def cameraStart(self):
        self.cam_thread.running = True
        self.cam_thread.start() # start Thread
        self.camera = cv2.VideoCapture(-1)
    
    def cameraStop(self):
        self.cam_thread.running = False
        self.camera.release

    def updateCamera(self):
        retval, image = self.camera.read()
        if retval:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h,w,c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)
            
            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
    

    '-----------------------VIDEO------------------'
    def clickVideo(self):
        self.videoStop()

    def videoStart(self):
        self.vid_thread.running = True
        self.vid_thread.start()
        self.videobtn.show()
        self.videobtn.setText("video stop")

    def videoStop(self):
        self.vid_thread.running = False
        self.video.release
        self.videobtn.setText("video start")

    
    def updateVideo(self):
        retval, image = self.video.read()
        if retval:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h,w,c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)
            
            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
            

    '----------------------CAPTURE--------------------------'
    def capture(self):
        retval, image = self.camera.read()
        if retval:
            self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = self.now + '.png'
            cv2.imwrite(filename, image)


class SendSignal(QThread):  # 매 1초마다 시그널을 보내는 쓰레드를 만듬
    update = pyqtSignal()

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = True
    
    def run(self):
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