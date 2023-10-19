import sys
import cv2, imutils
import datetime
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *


from_class = uic.loadUiType("cameraApp.ui")[0]
oldx = oldy = -1
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
        self.R_or_H.hide()
        self.G_or_S.hide()
        self.B_or_V.hide()
        self.RGB.hide()
        self.HSV.hide()
        self.draw.hide()
        
        '-------declare slider------'

        self.R_or_H.setRange(0, 179)
        self.R_or_H.setSingleStep(1)

        self.G_or_S.setRange(0, 255)
        self.G_or_S.setSingleStep(1)

        self.B_or_V.setRange(0, 255)
        self.B_or_V.setSingleStep(1)

        '----------declare pixmap------'
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

        '---------------HSV-----------'
        self.HSV.clicked.connect(self.changetoHSV)

        self.CHANGE_TO_HSV = False
        
        '--------------RGB------------'
        self.RGB.clicked.connect(self.changetoRGB)
        self.CHANGE_TO_RGB = False

        '-------------DRAW-------------'
        self.draw.clicked.connect(self.setDrawMode)
        self.DrawMode = False
        self.past_x = None
        self.past_y = None
        self.present_x = None
        self.present_y = None
    
    
    def openFile(self):

        file_name = QFileDialog.getOpenFileName(self, 'open file', './')

        if file_name[0].split('.')[1] in ['avi', 'mp4']: 
            self.video = cv2.VideoCapture(file_name[0])
            self.videoStart()

        else:
            self.draw.show()

            image = cv2.imread(file_name[0])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h,w,c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
            
            self.label.setPixmap(self.pixmap)
    

    '-----------------------RECORD---------------------'
    def clickRecord(self):
        if self.isRecStart == False:
            self.recordbtn.setText('Record Stop')
            self.isRecStart = True

            self.recordingStart()

        else:
            self.recordbtn.setText('Record Start')
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

            if self.CHANGE_TO_HSV == True:
                self.HSV.hide()
                image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
                H,S,V = cv2.split(image)
                h_value = self.R_or_H.value()
                s_value = self.G_or_S.value()
                v_value = self.B_or_V.value()

                H = H +h_value
                S = S +s_value
                V = V +v_value

                image = cv2.merge((H,S,V))
            else:
                R,G,B = cv2.split(image)
                r_value = self.R_or_H.value()
                g_value = self.G_or_S.value()
                b_value = self.B_or_V.value()

                R = R +r_value
                G = G +g_value
                B = B +b_value

                image = cv2.merge((R,G,B))

            self.writer.write(image)

    def keyReleaseEvent(self,e): #키를 누른상태에서 뗏을 때 실행됨
        if e.key() == Qt.Key_A:
            if self.isRecStart == False:
                self.recordbtn.setText('Record Stop')
                self.isRecStart = True

                self.recordingStart()

            else:
                self.recordbtn.setText('Record Start')
                self.isRecStart = False

                self.recordingStop()
    
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
        self.R_or_H.show()
        self.G_or_S.show()
        self.B_or_V.show()

        self.HSV.show()
        self.draw.show()

        retval, image = self.camera.read()
        if retval:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            if self.CHANGE_TO_HSV == True:
                self.HSV.hide()
                image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
                H,S,V = cv2.split(image)
                h_value = self.R_or_H.value()
                s_value = self.G_or_S.value()
                v_value = self.B_or_V.value()

                H = H +h_value
                S = S +s_value
                V = V +v_value

                image = cv2.merge((H,S,V))
            else:
                R,G,B = cv2.split(image)
                r_value = self.R_or_H.value()
                g_value = self.G_or_S.value()
                b_value = self.B_or_V.value()

                R = R +r_value
                G = G +g_value
                B = B +b_value

                image = cv2.merge((R,G,B))
                
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
        self.R_or_H.show()
        self.G_or_S.show()
        self.B_or_V.show()
        
        self.HSV.show()
        self.draw.show()

        retval, image = self.video.read()
        if retval:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            if self.CHANGE_TO_HSV == True:
                self.HSV.hide()
                image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
                
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
    


    '---------------------CHANGE HSV or RGB---------------------'
    def changetoHSV(self):
        self.RGB.show()
        
        self.label_2.setText("H")
        self.label_3.setText("S")
        self.label_4.setText("V")

        self.CHANGE_TO_HSV = True


    def changetoRGB(self):
        self.RGB.hide()
    
        self.label_2.setText("R")
        self.label_3.setText("G")
        self.label_4.setText("B")

        self.CHANGE_TO_HSV = False
    

    '------------------DRAW PICTURE---------------------'
    def setDrawMode(self):
        if self.DrawMode == False:
            self.DrawMode = True
            self.color = QColorDialog.getColor()
            self.draw.setText('stop draw')

        else:
            self.DrawMode = False
            self.draw.setText('draw')
    
    def mouseMoveEvent(self, event):
        self.drawLine(event.x(),event.y())

    def mouseReleaseEvent(self, event):

        self.past_x = None
        self.past_y = None
    
    def drawLine(self, x, y):
        if self.past_x is None:
            self.past_x = x
            self.past_y = y
        else:
            self.present_x = x
            self.present_y = y

            if self.DrawMode == True:
                painter = QPainter(self.label.pixmap())
                
                self.pen = QPen(self.color, 5, Qt.SolidLine)
                painter.setPen(self.pen)
                painter.drawLine(self.past_x, self.past_y,
                                  self.present_x, self.present_y)
                painter.end()
                self.update()

            self.past_x = self.present_x
            self.past_y = self.present_y




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