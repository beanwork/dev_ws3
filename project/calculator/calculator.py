import sys
import re
import traceback
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("calculator.ui")[0]
operator =["+", "-", "*", "/"]

class WindowClass (QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.pushButton_18.clicked.connect(self.button0_Clicked)  ## 0
        self.pushButton_10.clicked.connect(self.button1_Clicked)  ## 1
        self.pushButton_5.clicked.connect(self.button2_Clicked)  ## 2
        self.pushButton_6.clicked.connect(self.button3_Clicked)   ## 3
        self.pushButton_7.clicked.connect(self.button4_Clicked)   ## 4
        self.pushButton_11.clicked.connect(self.button5_Clicked)   ## 5
        self.pushButton_9.clicked.connect(self.button6_Clicked)   ## 6
        self.pushButton_4.clicked.connect(self.button7_Clicked)   ## 7
        self.pushButton_8.clicked.connect(self.button8_Clicked)   ## 8
        self.pushButton_12.clicked.connect(self.button9_Clicked)   ## 9
        self.pushButton.clicked.connect(self.buttonC_Clicked)   ## C
        self.pushButton_20.clicked.connect(self.buttonequal_Clicked)   ## =
        self.pushButton_3.clicked.connect(self.buttonpercent_Clicked)   ## %
        self.pushButton_17.clicked.connect(self.buttonconversion_Clicked)   ## +/--
        self.pushButton_19.clicked.connect(self.buttonpoint_Clicked)   ## .
        self.pushButton_16.clicked.connect(self.buttonadd_Clicked)   ## +
        self.pushButton_15.clicked.connect(self.buttonsubtract_Clicked)   ## --
        self.pushButton_14.clicked.connect(self.buttonmultiply_Clicked)   ## X
        self.pushButton_13.clicked.connect(self.buttondivision_Clicked)   ## /
        self.pushButton_21.clicked.connect(self.buttonbackspace_Clicked)   ## <--
        self.pushButton_2.clicked.connect(self.buttonbrace_Clicked)   ## ()
        

    def button0_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "0"
        self.lineEdit.setText(new_txt)

    def button1_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "1"
        self.lineEdit.setText(new_txt)

    def button2_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "2"
        self.lineEdit.setText(new_txt)

    def button3_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "3"
        self.lineEdit.setText(new_txt)

    def button4_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "4"
        self.lineEdit.setText(new_txt)

    def button5_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "5"
        self.lineEdit.setText(new_txt)

    def button6_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "6"
        self.lineEdit.setText(new_txt)

    def button7_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "7"
        self.lineEdit.setText(new_txt)

    def button8_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "8"
        self.lineEdit.setText(new_txt)

    def button9_Clicked(self):
        current_txt = self.lineEdit.text()
        new_txt = current_txt + "9"
        self.lineEdit.setText(new_txt)

    def buttonC_Clicked(self):
        self.lineEdit.clear()
    
    def calculate(self, formula):
        if '%' in formula:
            formula = formula.replace('%', '*0.01')

        if ')(' in formula:
            formula = formula.replace(')(', ')*(')

        if '()' in formula:
            formula = formula.replace('()', '(0)')
        
        try:
            result= eval(formula)

            return result
        
        except Exception as e:
            return e
                    
    def buttonequal_Clicked(self):
        current_txt = self.lineEdit.text()

        if current_txt == "":
            self.lineEdit_2.setText("enter formula")

        else:
            self.lineEdit_2.setText(self.lineEdit.text())
            self.lineEdit.clear()
            result = str(self.calculate(self.lineEdit_2.text()))
            
            if len(result) > 25:  ## output 25 digits 
                result = result[:25]

            self.lineEdit.setText(result)
        
    def buttonpercent_Clicked(self):
        global operator
        
        current_txt = self.lineEdit.text()

        if current_txt == "" or current_txt[-1] in operator:
            pass
        else:
            new_txt = current_txt + '%'
            self.lineEdit.setText(new_txt)

    def buttonconversion_Clicked(self):
        current_txt = self.lineEdit.text()

        numbers = re.findall(r'\d+', current_txt)
        operators = re.findall(r'[+\-*/]', current_txt)

        if current_txt == "":
            self.lineEdit.setText("-")
        elif current_txt == "-":
            pass
        elif operators or numbers:
            new_txt = '-1*(' + current_txt + ')'
            self.lineEdit.setText(new_txt)

    def buttonpoint_Clicked(self):
        global operator

        current_txt = self.lineEdit.text()
        
        add_count = current_txt.count('+')
        sub_count = current_txt.count('-')
        mul_count = current_txt.count('*')
        div_count = current_txt.count('/')

        operator_count = add_count + sub_count + mul_count + div_count
        point_count = current_txt.count('.')

        if current_txt == "" or current_txt[-1] in operator:
            new_txt = current_txt + '0.'
            self.lineEdit.setText(new_txt)
        else:
            if point_count <= operator_count:
                new_txt = current_txt + '.'
                self.lineEdit.setText(new_txt)
            else:
                pass    


    def buttonadd_Clicked(self):
        global operator

        current_txt = self.lineEdit.text()
        if current_txt == "" or current_txt[-1] in operator:
            pass
        else:
            new_txt = current_txt + '+'
            self.lineEdit.setText(new_txt)
            
    def buttonsubtract_Clicked(self):
        global operator

        current_txt = self.lineEdit.text()
        if current_txt == "" or current_txt[-1] in operator:
            pass
        else:
            new_txt = current_txt + '-'
            self.lineEdit.setText(new_txt)

    def buttonmultiply_Clicked(self):
        global operator

        current_txt = self.lineEdit.text()        
        if current_txt == "" or current_txt[-1] in operator:
            pass
        else:
            new_txt = current_txt + '*'
            self.lineEdit.setText(new_txt)
    
    def buttondivision_Clicked(self):
        global operator

        current_txt = self.lineEdit.text()            
        if current_txt == "" or current_txt[-1] in operator:
            pass    
        else:
            new_txt = current_txt + '/'
            self.lineEdit.setText(new_txt)
    
    def buttonbackspace_Clicked(self):
        current_txt = self.lineEdit.text() 
        new_txt = current_txt[:-1]

        self.lineEdit.setText(new_txt)
    
    def buttonbrace_Clicked(self):
        current_txt = self.lineEdit.text() 

        if (current_txt == "") or ('(' in current_txt) or (current_txt[-1] in operator): ## if not number, operator keep print '('
            new_txt = current_txt + '('
            self.lineEdit.setText(new_txt)

            numbers = re.findall(r'\d+', current_txt)
            operators = re.findall(r'[+\-*/]', current_txt)

            left_brace_count = current_txt.count('(')
            right_brace_count = current_txt.count(')')

            if (len(numbers) > len(operators)) and (right_brace_count < left_brace_count): ## if an exact formula keep print ')'
                new_txt = current_txt + ')'                                                ## accoriding to the number of left_braces
                self.lineEdit.setText(new_txt)
            else:
                new_txt = current_txt + '('      ## if an unexact formula
                self.lineEdit.setText(new_txt)   ## keep print '('             
        else:
            pass
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()

    sys.exit(app.exec_())
    
