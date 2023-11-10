import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QRegExp, QTimer
import socket
import struct
from struct import Struct
import datetime

from_class = uic.loadUiType("tcp.ui")[0]

class WindowClass (QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("tcp_client.ui")

        self.connected = False

        # timer
        self.timer = QTimer(self)
        self.timer.start(500) # 시작하면 줄어듬

        range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegExp("^" + range + "\\." + range + "\\." +\
                          range + "\\." + range +"$")
        self.IPEdit.setValidator(QRegExpValidator(ipRegex, self))
        self.PortEdit.setValidator(QIntValidator())
        self.degree.setValidator(QIntValidator())
        self.sensor.setValidator(QIntValidator())

        self.Connectbtn.clicked.connect(self.connect)
        self.led21.clicked.connect(self.clickLED21)
        self.led22.clicked.connect(self.clickLED22)
        self.led23.clicked.connect(self.clickLED23)
        self.Move.clicked.connect(self.clickMove)
        self.timer.timeout.connect(self.timeout)  # 타이머에서 발생하는 신호를 함수에 연결
    
    def __del__(self):
        self.sock.close()
        self.connected = False

    def connect(self):
        ip = self.IPEdit.text()
        port = self.PortEdit.text()

        self.sock = socket.socket()
        self.sock.connect((ip, int(port)))

        self.connected = True
        self.format = Struct('@ii') # 파이썬 구조체와 C언어 구조체 끼리 변환하기 위해 포맥 형식 지정해줌
        
    def clickLED21(self):
        isOn = self.led21.isChecked()
        self.updateLED(21, isOn)

    def clickLED22(self):
        isOn = self.led22.isChecked()
        self.updateLED(22, isOn)

    def clickLED23(self):
        isOn = self.led23.isChecked()
        self.updateLED(23, isOn)

    def clickMove(self):
        degree = int(self.degree.text())
        self.updateLED(5, degree)
    
    def timeout(self):
        self.updateLED(34, 0)
    
    def updateLED(self, pin, status):
        if self.connected == True:
            data = self.format.pack(pin ,status)
            req = self.sock.send(data)
            rev = self.format.unpack(self.sock.recv(self.format.size))
            if rev[0] == 34:
                self.sensor.setText(str(rev[1]))
            print(rev)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()

    sys.exit(app.exec_())
