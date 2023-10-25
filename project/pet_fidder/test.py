import time
from serial import Serial
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

from_class = uic.loadUiType("serial.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.conn = Serial(port='/dev/ttyACM0', baudrate=9600,timeout=0.1)
        self.serial = SerialManager(self.conn)
        self.serial.start()

        # self.send.clicked.connect(self.Send)
        '------------if instantly or set next Time button pressed -------------'
        self.giveInstantly.clicked.connect(self.GiveInstantly)
        self.setNextTime.clicked.connect(self.SetNextTime)
        '---------------next Time----------------------'
        self.hour.setRange(0, 8)
        self.hour.setSingleStep(1)
        # self.hour.valueChanged.connect(self.setNextHour)
        
        self.minute.setRange(0, 59)
        self.minute.setSingleStep(1)
        # self.minute.valueChanged.connect(self.setNextMinute)

        self.second.setRange(0, 59)
        self.second.setSingleStep(1)
        # self.second.valueChanged.connect(self.setNextSecond)
        '-------------response---------------'
        self.serial.receive.connect(self.Recv)
        
    def Send(self):
        text = self.lineEdit.text()
        text += "\n"
        self.conn.write(text.encode())

        #if self.conn.readable():
        #    res = self.conn.readline()
        #    self.textEdit.append(res.decode())
    
    def GiveInstantly(self):
        
        retval = QMessageBox.question(self, 'question', 'Are you sure give instantly?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if retval == QMessageBox.Yes:
            text = "give instantly"
            text += "\n"
            self.conn.write(text.encode())
        else:
            pass
        
    
    def SetNextTime(self):
        retval = QMessageBox.question(self, 'question', 'Are you sure set Next Time?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if retval == QMessageBox.Yes:
            text = "{0}H {1}M {2}S".format(self.hour.value(), self.minute.value(), self.second.value())
            text += "\n"
            
            self.conn.write(text.encode())
    
    # def setNextHour(self):
    #     self.hourValue = self.hour.value()
    # def setNextMinute(self):
    #     self.minuteValue = self.minute.value()
    # def setNextSecond(self):
    #     self.secondValue = self.second.value()
        

    def Recv(self, message):

        if message == "meal":
            QMessageBox.information(self,'notice','meals is given to your pet successfully')
        
        else:
            print(message)
            hms = message.split(" ")
            self.hourlabel.setText(hms[0])
            self.minutelabel.setText(hms[1])
            self.secondlabel.setText(hms[2])

            if (hms[0] == '0') and (hms[1] == '0') and (hms[2] == '0'):
                QMessageBox.information(self,'notice','meals is given to your pet successfully')



        # self.textEdit.append(message)
        


class SerialManager(QThread):
    receive = pyqtSignal(str)

    def __init__(self, serial=None):
        super().__init__()
        self.serial = serial
        self.running = True

    def run(self):
        while self.running == True:
            if self.serial.readable():
                res = self.serial.readline().decode()
                if len(res) > 0:
                    self.receive.emit(str(res))
            time.sleep(0.1)

    def stop(self):
        self.running = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())