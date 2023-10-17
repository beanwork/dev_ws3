import sys
import mysql.connector
from datetime import datetime 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("exercise.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton.clicked.connect(self.search)

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

    def make_query(self, sex='', jobtitle='', agency=''):
        if sex == 'M':
            sex_query = 'sex = "M"'
        elif sex == 'F':
            sex_query = 'sex = "F"'
        else:
            sex_query = None
        
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
            job_query = None
        
        if 'EDAM엔터테이먼트' in agency:
            agency_query = 'agency = "EDAM엔터테이먼트"'
        elif '울림엔터테이먼트' in agency:
            agency_query = 'agency = "울림엔터테이먼트"'
        elif '나무엑터스' in agency:
            agency_query = 'agency = "나무엑터스"'
        elif 'YG엔터테이먼트' in agency:
            agency_query = 'agency = "YG엔터테이먼트"'
        elif '안테나' in agency:
            agency_query = 'agency = "안테나"'
        else:
            agency_query = None

        final_query = self.make_finalquery(sex_query , job_query , agency_query)

        return  final_query

    def make_finalquery(self, sex_query , job_query , agency_query):
        if (not sex_query == None) and (not job_query == None) and (not agency_query == None): ## 다 not none일 때
            final_query = sex_query + ' and ' + job_query + ' and ' + agency_query 

        elif (sex_query == None) and (not job_query == None) and (not agency_query == None): 
            final_query = job_query + ' and ' + agency_query 
        
        elif (not sex_query == None) and (job_query == None) and (not agency_query == None): 
            final_query = sex_query + ' and ' + agency_query 
        
        elif (not sex_query == None) and (not job_query == None) and (agency_query == None):  ## 하나만 none일 때
            final_query = sex_query + ' and ' + job_query 
        
        elif (sex_query == None) and (job_query == None) and (not agency_query == None): 
            final_query = agency_query 
        
        elif (sex_query == None) and (not job_query == None) and (agency_query == None): 
            final_query = job_query  
        
        elif (not sex_query == None) and (job_query == None) and (agency_query == None):  ## 2개가 none일때 
            final_query = sex_query 

        else:
            final_query = None

        return final_query


    def search(self):
        self.set_birth()
        final_query  = self.make_query(self.comboBox.currentText(), self.comboBox_2.currentText(), self.comboBox_3.currentText())
        if not final_query == None :
            self.pyqt_cur.execute("select * from celeb where " + final_query)
        self.pyqt_con.commit()

        pyqt_result = self.pyqt_cur.fetchall()

        if pyqt_result != None:
            self.tableWidget.setRowCount(0)
            for row, celeb_info in enumerate(pyqt_result):
                self.tableWidget.insertRow(row)
                for idx, info in enumerate(celeb_info):
                    self.tableWidget.setItem(row, idx, QTableWidgetItem(str(info)))
                    print(type(self.dateEdit.text()))
    
    def set_birth(self):
        self.pyqt_cur.execute("Select min(birth) from celeb;")
        min_birth = self.pyqt_cur.fetchall()[0]
        
        self.pyqt_cur.execute("select max(birth) from celeb;")
        max_birth = self.pyqt_cur.fetchall()[0]

        start_date = datetime.strptime(self.dateEdit.text(), '%Y%m%d').date()
        end_date = datetime.strptime(self.dateEdit_2.text(), '%Y%m%d').date()

        if start_date > end_date :
            QMessageBox.information(self, "날짜 오류", "date에 오류가 있습니다.")
            self.dateEdit.setText(str(min_birth))
            self.dateEdit_2.setText(str(max_birth))
   
            
    def __del__(self):
        self.pyqt_con.close()

       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
    
    