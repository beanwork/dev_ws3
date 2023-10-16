import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("exercise.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton.clicked.connect(self.show_table)

        for sex in ["M", "F", "Others"]:
            self.comboBox.addItem(sex)

        for jobTitle in ['가수', '텔런트', 'MC', '개그맨', '영화배우', '모델']:
            self.comboBox_2.addItem(jobTitle)

        for agency in ['EDAM엔터테이먼트', '울림엔터테이먼트', '나무엑터스', 'YG엔터테이먼트','안테나']:
            self.comboBox_3.addItem(agency)
        
        self.pyqt_con = mysql.connector.connect(
        host = "database-1.cmdlhagy2um9.ap-northeast-2.rds.amazonaws.com",
        port = 3306,
        user = "admin", 
        password = "dltnals123$",
        database = "armbase"
        )
        self.pyqt_cur = self.pyqt_con.cursor(buffered=True)

    def make_query(self, sex=None, jobtitle = None, agency = None):
        if sex == 'M':
            sex_query = 'sex = "M"'
        elif sex == 'F':
            sex_query = 'sex = "F"'
        else:
            pass
        
        if '가수' in jobtitle:
            job_query = 'job like "%가수%"'
        elif '텔런트' in jobtitle:
            job_query = 'job like "%텔런트%"'
        elif 'MC' in jobtitle:
            job_query = 'job like "%MC%"'
        elif '개그맨' in jobtitle:
            job_query = 'job like "%개그맨%"'
        elif '영화배우' in jobtitle:
            job_query = 'job like "%영화배우%"'
        elif '모델' in jobtitle:
            job_query = 'job like "%모델%"'
        else:
            pass
        
        if 'EDAM엔터테이먼트' in agency:
            agency_query = 'agency = "EDAM엔터테이먼트"'
        elif '울림엔터테이먼트' in agency:
            agency_query = 'agency = "울림엔터테이먼트"'
        elif '나무엑터스' in agency:
            agency_query = 'agency = "나무엑터스"'
        elif 'YG엔터테이먼트' in agency:
            agency_query = 'agency = "YG엔터테이먼트"'
        elif '안테나' in agency:
            agency_query = 'and agency = "안테나"'
        else:
            pass

        return sex_query , job_query , agency_query        

    def show_table(self):

        sex_query , job_query , agency_query  = self.make_query(self.comboBox.currentText(), 
                                                                self.comboBox_2.currentText(),
                                                                self.comboBox_3.currentText())
        if not sex_query  and  not job_query  and not agency_query :
            final_query = sex_query + ' and ' + job_query + ' and '+ agency_query
            print(final_query)
            self.pyqt_cur.execute("select * from celeb where " + final_query)
        self.pyqt_con.commit()

        pyqt_result = self.pyqt_cur.fetchall()

        if pyqt_result != None:
            for celeb_info in pyqt_result:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for idx, info in enumerate(celeb_info):
                    self.tableWidget.setItem(row, idx, QTableWidgetItem(str(info)))
        
    
    def __del__(self):
        self.pyqt_con.close()

       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
    
    