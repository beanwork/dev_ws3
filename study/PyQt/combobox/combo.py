import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("combobox.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for year in range(1900, 2023):
            self.comboBox.addItem(str(year))

        for month in range(1, 13):
            self.comboBox_2.addItem(str(month))
        
        for day in range(1, 32):
            self.comboBox_3.addItem(str(day))

        self.comboBox.setCurrentText(str(1990))
        self.comboBox_3.currentIndexChanged.connect(self.printBirthday)
        self.calendarWidget.clicked.connect(self.selectDate)
    
    def printBirthday(self):
        year = self.comboBox.currentText()
        month = self.comboBox_2.currentText()
        day = self.comboBox_3.currentText()

        self.lineEdit.setText(year+month.zfill(2)+day.zfill(2))
    
    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString('yyyy')
        month = date.toString('M')
        day = date.toString('d')

        self.comboBox.setCurrentText(year)
        self.comboBox_2.setCurrentText(month)
        self.comboBox_3.setCurrentText(day)

        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindows = WindowClass()
    mywindows.show()
    sys.exit(app.exec_())