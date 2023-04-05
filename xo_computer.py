import os
os.system("cls")

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("X/O suniy intelect")

        # self.setMinimumSize(200,200)

        self.winner = list()

        self.list = list()

        self.h_box1 = QHBoxLayout()
        
        self.h_box2 = QHBoxLayout()
        
        
        self.h_box3 = QHBoxLayout()

        self.v_box =  QVBoxLayout()

        self.tyr_again_box = QHBoxLayout()

        self.tag = QLabel(self)

        self.count = 0


        # BUTTONS
        self.btn_1 = QPushButton(self)
        self.btn_1.setFixedSize(60,60)
        # self.btn_1.setStyleSheet("background-color:	#C6E2FF")

        self.btn_1.setStyleSheet('QPushButton::hover'"{""background-color : #BBFFFF" "}")
        

        self.btn_2 = QPushButton(self)
        # self.btn_2.setText('  ')
        self.btn_2.setFixedSize(60,60)
        # self.btn_2.setStyleSheet("background-color: #C6E2FF")
        self.btn_2.setStyleSheet('QPushButton::hover'"{""background-color : 	#EEAEEE" "}")

        self.btn_3 = QPushButton(self)
        # self.btn_3.setText('  ')
        self.btn_3.setFixedSize(60,60)
        # self.btn_3.setStyleSheet("background-color: #C6E2FF ")
        self.btn_3.setStyleSheet('QPushButton::hover'"{""background-color : 	#4EEE94" "}")

        self.btn_4 = QPushButton(self)
        # self.btn_4.setText('  ')
        self.btn_4.setFixedSize(60,60)
        # self.btn_4.setStyleSheet("background-color: #C6E2FF ")
        self.btn_4.setStyleSheet('QPushButton::hover'"{""background-color : #836FFF" "}")

        self.btn_5 = QPushButton(self)
        # self.btn_5.setText('  ')
        self.btn_5.setFixedSize(60,60)
        # self.btn_5.setStyleSheet("background-color: #C6E2FF ")
        self.btn_5.setStyleSheet('QPushButton::hover'"{""background-color : #EEEE00" "}")

        self.btn_6 = QPushButton(self)
        # self.btn_6.setText('  ')
        self.btn_6.setFixedSize(60,60)
        # self.btn_6.setStyleSheet("background-color: #C6E2FF ")
        self.btn_6.setStyleSheet('QPushButton::hover'"{""background-color :	#EE7942" "}")

        self.btn_7 = QPushButton(self)
        # self.btn_7.setText('  ')
        self.btn_7.setFixedSize(60,60)
        # self.btn_7.setStyleSheet("background-color: #C6E2FF ")
        self.btn_7.setStyleSheet('QPushButton::hover'"{""background-color :	#EECBAD" "}")

        self.btn_8 = QPushButton(self)
        # self.btn_8.setText('  ')
        self.btn_8.setFixedSize(60,60)
        # self.btn_8.setStyleSheet("background-color: #C6E2FF")
        self.btn_8.setStyleSheet('QPushButton::hover'"{""background-color : #D15FEE" "}")

        self.btn_9 = QPushButton(self)
        # self.btn_9.setText('  ')
        self.btn_9.setFixedSize(60,60)
        # self.btn_9.setStyleSheet("background-color: #C6E2FF")
        self.btn_9.setStyleSheet('QPushButton::hover'"{""background-color :#CAE1FF" "}")

        self.btn_try_agin = QPushButton(self)
        self.btn_try_agin.setText('Try again')
        self.btn_try_agin.setFixedSize(70,30)


        self.h_box1.addWidget(self.btn_1)
        self.h_box1.addWidget(self.btn_2)
        self.h_box1.addWidget(self.btn_3)


        self.h_box2.addWidget(self.btn_4)
        self.h_box2.addWidget(self.btn_5)
        self.h_box2.addWidget(self.btn_6)
                
        self.h_box3.addWidget(self.btn_7)
        self.h_box3.addWidget(self.btn_8)
        self.h_box3.addWidget(self.btn_9)

        self.tyr_again_box.addWidget(self.btn_try_agin)


        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.tyr_again_box)

        self.setLayout(self.v_box)

        self.show()

        self.btn_1.clicked.connect(self.press_btn1)
        self.btn_2.clicked.connect(self.press_btn2)
        self.btn_3.clicked.connect(self.press_btn3)
        self.btn_4.clicked.connect(self.press_btn4)
        self.btn_5.clicked.connect(self.press_btn5)
        self.btn_6.clicked.connect(self.press_btn6)
        self.btn_7.clicked.connect(self.press_btn7)
        self.btn_8.clicked.connect(self.press_btn8)
        self.btn_9.clicked.connect(self.press_btn9)


        # SUNIY INTELECT

        # FIRST BUTTONS

        self.btn_1.clicked.connect(self.press_first_btn1)
        self.btn_2.clicked.connect(self.press_first_btn2)
        self.btn_3.clicked.connect(self.press_first_btn3)
        self.btn_4.clicked.connect(self.press_first_btn4)
        self.btn_5.clicked.connect(self.press_first_btn5)
        self.btn_6.clicked.connect(self.press_first_btn6)
        self.btn_7.clicked.connect(self.press_first_btn7)
        self.btn_8.clicked.connect(self.press_first_btn8)
        self.btn_9.clicked.connect(self.press_first_btn9)

        # SECOND BUTTONS

        self.btn_2.clicked.connect(self.press_second_btn5_2)
        self.btn_3.clicked.connect(self.press_second_btn5_3)
        self.btn_4.clicked.connect(self.press_second_btn5_4)
        self.btn_6.clicked.connect(self.press_second_btn5_6)
        self.btn_7.clicked.connect(self.press_second_btn5_7)
        self.btn_8.clicked.connect(self.press_second_btn5_8)
        self.btn_9.clicked.connect(self.press_second_btn5_9)



        self.btn_3.clicked.connect(self.press_second1_3)
        self.btn_2.clicked.connect(self.press_second1_2)
        self.btn_4.clicked.connect(self.press_second1_4)
        self.btn_6.clicked.connect(self.press_second1_6)
        self.btn_7.clicked.connect(self.press_second1_7)
        self.btn_8.clicked.connect(self.press_second1_8)
        self.btn_9.clicked.connect(self.press_second1_9)



        self.btn_1.clicked.connect(self.press_btn2_1)
        self.btn_3.clicked.connect(self.press_btn2_3)
        self.btn_4.clicked.connect(self.press_btn2_4)
        self.btn_6.clicked.connect(self.press_btn2_6)
        self.btn_7.clicked.connect(self.press_btn2_7)
        self.btn_8.clicked.connect(self.press_btn2_8)
        self.btn_9.clicked.connect(self.press_btn2_9)


        self.btn_1.clicked.connect(self.press_btn3_1)
        self.btn_2.clicked.connect(self.press_btn3_2)
        self.btn_4.clicked.connect(self.press_btn3_4)
        self.btn_6.clicked.connect(self.press_btn3_6)
        self.btn_7.clicked.connect(self.press_btn3_7)
        self.btn_8.clicked.connect(self.press_btn3_8)
        self.btn_9.clicked.connect(self.press_btn3_9)


        self.btn_1.clicked.connect(self.press_btn4_1)
        self.btn_2.clicked.connect(self.press_btn4_2)
        self.btn_3.clicked.connect(self.press_btn4_3)
        self.btn_6.clicked.connect(self.press_btn4_6)
        self.btn_7.clicked.connect(self.press_btn4_7)
        self.btn_8.clicked.connect(self.press_btn4_8)
        self.btn_9.clicked.connect(self.press_btn4_9)



        self.btn_1.clicked.connect(self.press_btn6_1)
        self.btn_2.clicked.connect(self.press_btn6_2)
        self.btn_3.clicked.connect(self.press_btn6_3)
        self.btn_4.clicked.connect(self.press_btn6_4)
        self.btn_7.clicked.connect(self.press_btn6_7)
        self.btn_8.clicked.connect(self.press_btn6_8)
        self.btn_9.clicked.connect(self.press_btn6_9)


        self.btn_1.clicked.connect(self.press_btn7_1)
        self.btn_2.clicked.connect(self.press_btn7_2)
        self.btn_3.clicked.connect(self.press_btn7_3)
        self.btn_4.clicked.connect(self.press_btn7_4)
        self.btn_6.clicked.connect(self.press_btn7_6)
        self.btn_8.clicked.connect(self.press_btn7_8)
        self.btn_9.clicked.connect(self.press_btn7_9)




        self.btn_1.clicked.connect(self.press_btn8_1)
        self.btn_2.clicked.connect(self.press_btn8_2)
        self.btn_3.clicked.connect(self.press_btn8_3)
        self.btn_4.clicked.connect(self.press_btn8_4)
        self.btn_6.clicked.connect(self.press_btn8_6)
        self.btn_7.clicked.connect(self.press_btn8_7)
        self.btn_9.clicked.connect(self.press_btn8_9)



        self.btn_1.clicked.connect(self.press_btn9_1)
        self.btn_2.clicked.connect(self.press_btn9_2)
        self.btn_3.clicked.connect(self.press_btn9_3)
        self.btn_4.clicked.connect(self.press_btn9_4)
        self.btn_6.clicked.connect(self.press_btn9_6)
        self.btn_7.clicked.connect(self.press_btn9_7)
        self.btn_8.clicked.connect(self.press_btn9_8)

        

        self.btn_4.clicked.connect(self.press_third_btn1_2_4)
        self.btn_6.clicked.connect(self.press_third_btn1_2_6)
        self.btn_8.clicked.connect(self.press_third_btn1_2_8)
        self.btn_9.clicked.connect(self.press_third_btn1_2_9)
        self.btn_7.clicked.connect(self.press_third_btn1_2_7)


        self.btn_4.clicked.connect(self.press_third_btn1_3_4)
        self.btn_6.clicked.connect(self.press_third_btn1_3_6)
        self.btn_7.clicked.connect(self.press_third_btn1_3_7)
        self.btn_8.clicked.connect(self.press_third_btn1_3_8)
        self.btn_9.clicked.connect(self.press_third_btn1_3_9)


        self.btn_2.clicked.connect(self.press_third_btn1_4_2)
        self.btn_6.clicked.connect(self.press_third_btn1_4_6)
        self.btn_8.clicked.connect(self.press_third_btn1_4_8)
        self.btn_9.clicked.connect(self.press_third_btn1_4_9)
        self.btn_3.clicked.connect(self.press_third_btn1_4_3)
    

        self.btn_3.clicked.connect(self.press_third_btn1_6_3)
        self.btn_4.clicked.connect(self.press_third_btn1_6_4)
        self.btn_7.clicked.connect(self.press_third_btn1_6_7)
        self.btn_9.clicked.connect(self.press_third_btn1_6_9)
        self.btn_8.clicked.connect(self.press_third_btn1_6_8)



        self.btn_2.clicked.connect(self.press_third_btn1_7_2)
        self.btn_3.clicked.connect(self.press_third_btn1_7_3)
        self.btn_8.clicked.connect(self.press_third_btn1_7_8)
        self.btn_9.clicked.connect(self.press_third_btn1_7_9)
        self.btn_6.clicked.connect(self.press_third_btn1_7_6)


        self.btn_2.clicked.connect(self.press_third_btn1_8_2)
        self.btn_3.clicked.connect(self.press_third_btn1_8_3)
        self.btn_7.clicked.connect(self.press_third_btn1_8_7)
        self.btn_9.clicked.connect(self.press_third_btn1_8_9)
        self.btn_6.clicked.connect(self.press_third_btn1_8_6)


        self.btn_3.clicked.connect(self.press_third_btn1_9_3)
        self.btn_4.clicked.connect(self.press_third_btn1_9_4)
        self.btn_6.clicked.connect(self.press_third_btn1_9_6)
        self.btn_7.clicked.connect(self.press_third_btn1_9_7)
        self.btn_8.clicked.connect(self.press_third_btn1_9_8)


        self.btn_4.clicked.connect(self.press_third_btn2_1_4)
        self.btn_6.clicked.connect(self.press_third_btn2_1_6)
        self.btn_8.clicked.connect(self.press_third_btn2_1_8)
        self.btn_9.clicked.connect(self.press_third_btn2_1_9)
        self.btn_7.clicked.connect(self.press_third_btn2_1_7)


        self.btn_4.clicked.connect(self.press_third_btn2_3_4)
        self.btn_6.clicked.connect(self.press_third_btn2_3_6)
        self.btn_7.clicked.connect(self.press_third_btn2_3_7)
        self.btn_8.clicked.connect(self.press_third_btn2_3_8)
        self.btn_9.clicked.connect(self.press_third_btn2_3_9)


        self.btn_1.clicked.connect(self.press_third_btn2_4_1)
        self.btn_6.clicked.connect(self.press_third_btn2_4_6)
        self.btn_8.clicked.connect(self.press_third_btn2_4_8)
        self.btn_9.clicked.connect(self.press_third_btn2_4_9)
        self.btn_7.clicked.connect(self.press_third_btn2_4_7)


        self.btn_3.clicked.connect(self.press_third_btn2_6_3)
        self.btn_4.clicked.connect(self.press_third_btn2_6_4)
        self.btn_7.clicked.connect(self.press_third_btn2_6_7)
        self.btn_8.clicked.connect(self.press_third_btn2_6_8)
        self.btn_9.clicked.connect(self.press_third_btn2_6_9)


        self.btn_1.clicked.connect(self.press_third_btn2_7_1)
        self.btn_3.clicked.connect(self.press_third_btn2_7_3)
        self.btn_8.clicked.connect(self.press_third_btn2_7_8)
        self.btn_9.clicked.connect(self.press_third_btn2_7_9)
        self.btn_6.clicked.connect(self.press_third_btn2_7_6)



        self.btn_1.clicked.connect(self.press_third_btn2_8_1)
        self.btn_4.clicked.connect(self.press_third_btn2_8_4)
        self.btn_6.clicked.connect(self.press_third_btn2_8_6)
        self.btn_9.clicked.connect(self.press_third_btn2_8_9)
        self.btn_3.clicked.connect(self.press_third_btn2_8_3)


        self.btn_1.clicked.connect(self.press_third_btn2_9_1)
        self.btn_3.clicked.connect(self.press_third_btn2_9_3)
        self.btn_7.clicked.connect(self.press_third_btn2_9_7)
        self.btn_8.clicked.connect(self.press_third_btn2_9_8)
        self.btn_4.clicked.connect(self.press_third_btn2_9_4)


        self.btn_4.clicked.connect(self.press_third_btn3_1_4)
        self.btn_6.clicked.connect(self.press_third_btn3_1_6)
        self.btn_7.clicked.connect(self.press_third_btn3_1_7)
        self.btn_9.clicked.connect(self.press_third_btn3_1_9)
        self.btn_8.clicked.connect(self.press_third_btn3_1_8)


        
        self.btn_4.clicked.connect(self.press_third_btn3_2_4)
        self.btn_6.clicked.connect(self.press_third_btn3_2_6)
        self.btn_7.clicked.connect(self.press_third_btn3_2_7)
        self.btn_8.clicked.connect(self.press_third_btn3_2_8)
        self.btn_9.clicked.connect(self.press_third_btn3_2_9)


        self.btn_1.clicked.connect(self.press_third_btn3_4_1)
        self.btn_6.clicked.connect(self.press_third_btn3_4_6)
        self.btn_7.clicked.connect(self.press_third_btn3_4_7)
        self.btn_9.clicked.connect(self.press_third_btn3_4_9)
        self.btn_8.clicked.connect(self.press_third_btn3_4_8)


        self.btn_2.clicked.connect(self.press_third_btn3_6_2)
        self.btn_4.clicked.connect(self.press_third_btn3_6_4)
        self.btn_7.clicked.connect(self.press_third_btn3_6_7)
        self.btn_8.clicked.connect(self.press_third_btn3_6_8)
        self.btn_1.clicked.connect(self.press_third_btn3_6_1)


        self.btn_1.clicked.connect(self.press_third_btn3_7_1)
        self.btn_4.clicked.connect(self.press_third_btn3_7_4)
        self.btn_6.clicked.connect(self.press_third_btn3_7_6)
        self.btn_9.clicked.connect(self.press_third_btn3_7_9)
        self.btn_8.clicked.connect(self.press_third_btn3_7_8)


        self.btn_1.clicked.connect(self.press_third_btn3_8_1)
        self.btn_2.clicked.connect(self.press_third_btn3_8_2)
        self.btn_7.clicked.connect(self.press_third_btn3_8_7)
        self.btn_9.clicked.connect(self.press_third_btn3_8_9)
        self.btn_4.clicked.connect(self.press_third_btn3_8_4)


        self.btn_1.clicked.connect(self.press_third_btn3_9_1)
        self.btn_2.clicked.connect(self.press_third_btn3_9_2)
        self.btn_7.clicked.connect(self.press_third_btn3_9_7)
        self.btn_8.clicked.connect(self.press_third_btn3_9_8)
        self.btn_4.clicked.connect(self.press_third_btn3_9_4)


        self.btn_2.clicked.connect(self.press_third_btn4_1_2)
        self.btn_6.clicked.connect(self.press_third_btn4_1_6)
        self.btn_8.clicked.connect(self.press_third_btn4_1_8)
        self.btn_9.clicked.connect(self.press_third_btn4_1_9)
        self.btn_3.clicked.connect(self.press_third_btn4_1_3)

    
        self.btn_1.clicked.connect(self.press_third_btn4_2_1)
        self.btn_6.clicked.connect(self.press_third_btn4_2_6)
        self.btn_8.clicked.connect(self.press_third_btn4_2_8)
        self.btn_9.clicked.connect(self.press_third_btn4_2_9)
        self.btn_7.clicked.connect(self.press_third_btn4_2_7)


        self.btn_1.clicked.connect(self.press_third_btn4_3_1)
        self.btn_6.clicked.connect(self.press_third_btn4_3_6)
        self.btn_7.clicked.connect(self.press_third_btn4_3_7)
        self.btn_9.clicked.connect(self.press_third_btn4_3_9)
        self.btn_8.clicked.connect(self.press_third_btn4_3_8)


        self.btn_1.clicked.connect(self.press_third_btn4_6_1)
        self.btn_2.clicked.connect(self.press_third_btn4_6_2)
        self.btn_8.clicked.connect(self.press_third_btn4_6_8)
        self.btn_9.clicked.connect(self.press_third_btn4_6_9)
        self.btn_7.clicked.connect(self.press_third_btn4_6_7)


        self.btn_2.clicked.connect(self.press_third_btn4_7_2)
        self.btn_3.clicked.connect(self.press_third_btn4_7_3)
        self.btn_6.clicked.connect(self.press_third_btn4_7_6)
        self.btn_8.clicked.connect(self.press_third_btn4_7_8)
        self.btn_9.clicked.connect(self.press_third_btn4_7_9)


        self.btn_2.clicked.connect(self.press_third_btn4_8_2)
        self.btn_3.clicked.connect(self.press_third_btn4_8_3)
        self.btn_6.clicked.connect(self.press_third_btn4_8_6)
        self.btn_7.clicked.connect(self.press_third_btn4_8_7)
        self.btn_1.clicked.connect(self.press_third_btn4_8_1)


        self.btn_1.clicked.connect(self.press_third_btn4_9_1)
        self.btn_3.clicked.connect(self.press_third_btn4_9_3)
        self.btn_6.clicked.connect(self.press_third_btn4_9_6)
        self.btn_7.clicked.connect(self.press_third_btn4_9_7)
        self.btn_2.clicked.connect(self.press_third_btn4_9_2)


        self.btn_3.clicked.connect(self.press_third_btn5_2_3)
        self.btn_4.clicked.connect(self.press_third_btn5_2_4)
        self.btn_7.clicked.connect(self.press_third_btn5_2_7)
        self.btn_9.clicked.connect(self.press_third_btn5_2_9)
        self.btn_6.clicked.connect(self.press_third_btn5_2_6)


        self.btn_2.clicked.connect(self.press_third_btn5_3_2)
        self.btn_4.clicked.connect(self.press_third_btn5_3_4)
        self.btn_6.clicked.connect(self.press_third_btn5_3_6)
        self.btn_8.clicked.connect(self.press_third_btn5_3_8)
        self.btn_9.clicked.connect(self.press_third_btn5_3_9)


        self.btn_2.clicked.connect(self.press_third_btn5_4_2)
        self.btn_3.clicked.connect(self.press_third_btn5_4_3)
        self.btn_7.clicked.connect(self.press_third_btn5_4_7)
        self.btn_8.clicked.connect(self.press_third_btn5_4_8)
        self.btn_9.clicked.connect(self.press_third_btn5_4_9)


        self.btn_2.clicked.connect(self.press_third_btn5_6_2)
        self.btn_3.clicked.connect(self.press_third_btn5_6_3)
        self.btn_8.clicked.connect(self.press_third_btn5_6_8)
        self.btn_9.clicked.connect(self.press_third_btn5_6_9)
        self.btn_7.clicked.connect(self.press_third_btn5_6_7)


        self.btn_4.clicked.connect(self.press_third_btn5_7_4)
        self.btn_6.clicked.connect(self.press_third_btn5_7_6)
        self.btn_8.clicked.connect(self.press_third_btn5_7_8)
        self.btn_9.clicked.connect(self.press_third_btn5_7_9)
        self.btn_2.clicked.connect(self.press_third_btn5_7_2)


        self.btn_4.clicked.connect(self.press_third_btn5_8_4)
        self.btn_6.clicked.connect(self.press_third_btn5_8_6)
        self.btn_7.clicked.connect(self.press_third_btn5_8_7)
        self.btn_9.clicked.connect(self.press_third_btn5_8_9)
        self.btn_3.clicked.connect(self.press_third_btn5_8_3)


        self.btn_4.clicked.connect(self.press_third_btn5_9_4)
        self.btn_6.clicked.connect(self.press_third_btn5_9_6)
        self.btn_7.clicked.connect(self.press_third_btn5_9_7)
        self.btn_8.clicked.connect(self.press_third_btn5_9_8)
        self.btn_2.clicked.connect(self.press_third_btn5_9_2)


        self.btn_3.clicked.connect(self.press_third_btn6_1_3)
        self.btn_4.clicked.connect(self.press_third_btn6_1_4)
        self.btn_7.clicked.connect(self.press_third_btn6_1_7)
        self.btn_9.clicked.connect(self.press_third_btn6_1_9)
        self.btn_8.clicked.connect(self.press_third_btn6_1_8)



        self.btn_3.clicked.connect(self.press_third_btn6_2_3)
        self.btn_4.clicked.connect(self.press_third_btn6_2_4)
        self.btn_7.clicked.connect(self.press_third_btn6_2_7)
        self.btn_8.clicked.connect(self.press_third_btn6_2_8)
        self.btn_9.clicked.connect(self.press_third_btn6_2_9)


        self.btn_2.clicked.connect(self.press_third_btn6_3_2)
        self.btn_4.clicked.connect(self.press_third_btn6_3_4)
        self.btn_7.clicked.connect(self.press_third_btn6_3_7)
        self.btn_8.clicked.connect(self.press_third_btn6_3_8)
        self.btn_1.clicked.connect(self.press_third_btn6_3_1)



        self.btn_1.clicked.connect(self.press_third_btn6_4_1)
        self.btn_2.clicked.connect(self.press_third_btn6_4_2)
        self.btn_8.clicked.connect(self.press_third_btn6_4_8)
        self.btn_9.clicked.connect(self.press_third_btn6_4_9)
        self.btn_7.clicked.connect(self.press_third_btn6_4_7)


        self.btn_1.clicked.connect(self.press_third_btn6_7_1)
        self.btn_3.clicked.connect(self.press_third_btn6_7_3)
        self.btn_4.clicked.connect(self.press_third_btn6_7_4)
        self.btn_9.clicked.connect(self.press_third_btn6_7_9)
        self.btn_2.clicked.connect(self.press_third_btn6_7_2)


        self.btn_1.clicked.connect(self.press_third_btn6_8_1)
        self.btn_2.clicked.connect(self.press_third_btn6_8_2)
        self.btn_4.clicked.connect(self.press_third_btn6_8_4)
        self.btn_9.clicked.connect(self.press_third_btn6_8_9)
        self.btn_3.clicked.connect(self.press_third_btn6_8_3)

    
        self.btn_1.clicked.connect(self.press_third_btn6_9_1)
        self.btn_2.clicked.connect(self.press_third_btn6_9_2)
        self.btn_4.clicked.connect(self.press_third_btn6_9_4)
        self.btn_8.clicked.connect(self.press_third_btn6_9_8)
        self.btn_7.clicked.connect(self.press_third_btn6_9_7)


        self.btn_2.clicked.connect(self.press_third_btn7_1_2)
        self.btn_3.clicked.connect(self.press_third_btn7_1_3)
        self.btn_8.clicked.connect(self.press_third_btn7_1_8)
        self.btn_9.clicked.connect(self.press_third_btn7_1_9)
        self.btn_6.clicked.connect(self.press_third_btn7_1_6)



        self.btn_1.clicked.connect(self.press_third_btn7_2_1)
        self.btn_3.clicked.connect(self.press_third_btn7_2_3)
        self.btn_8.clicked.connect(self.press_third_btn7_2_8)
        self.btn_9.clicked.connect(self.press_third_btn7_2_9)
        self.btn_6.clicked.connect(self.press_third_btn7_2_6)


        self.btn_1.clicked.connect(self.press_third_btn7_3_1)
        self.btn_4.clicked.connect(self.press_third_btn7_3_4)
        self.btn_6.clicked.connect(self.press_third_btn7_3_6)
        self.btn_9.clicked.connect(self.press_third_btn7_3_9)
        self.btn_8.clicked.connect(self.press_third_btn7_3_8)


        self.btn_2.clicked.connect(self.press_third_btn7_4_2)
        self.btn_6.clicked.connect(self.press_third_btn7_4_6)
        self.btn_3.clicked.connect(self.press_third_btn7_4_3)
        self.btn_8.clicked.connect(self.press_third_btn7_4_8)
        self.btn_9.clicked.connect(self.press_third_btn7_4_9)


        self.btn_1.clicked.connect(self.press_third_btn7_6_1)
        self.btn_3.clicked.connect(self.press_third_btn7_6_3)
        self.btn_4.clicked.connect(self.press_third_btn7_6_4)
        self.btn_9.clicked.connect(self.press_third_btn7_6_9)
        self.btn_2.clicked.connect(self.press_third_btn7_6_2)


        self.btn_2.clicked.connect(self.press_third_btn7_8_2)
        self.btn_3.clicked.connect(self.press_third_btn7_8_3)
        self.btn_4.clicked.connect(self.press_third_btn7_8_4)
        self.btn_6.clicked.connect(self.press_third_btn7_8_6)
        self.btn_1.clicked.connect(self.press_third_btn7_8_1)



        self.btn_1.clicked.connect(self.press_third_btn7_9_1)
        self.btn_3.clicked.connect(self.press_third_btn7_9_3)
        self.btn_4.clicked.connect(self.press_third_btn7_9_4)
        self.btn_6.clicked.connect(self.press_third_btn7_9_6)
        self.btn_2.clicked.connect(self.press_third_btn7_9_2)


        self.btn_2.clicked.connect(self.press_third_btn8_1_2)
        self.btn_3.clicked.connect(self.press_third_btn8_1_3)
        self.btn_7.clicked.connect(self.press_third_btn8_1_7)
        self.btn_9.clicked.connect(self.press_third_btn8_1_9)
        self.btn_6.clicked.connect(self.press_third_btn8_1_6)


        self.btn_1.clicked.connect(self.press_third_btn8_2_1)
        self.btn_4.clicked.connect(self.press_third_btn8_2_4)
        self.btn_6.clicked.connect(self.press_third_btn8_2_6)
        self.btn_9.clicked.connect(self.press_third_btn8_2_9)
        self.btn_3.clicked.connect(self.press_third_btn8_2_3)


        self.btn_1.clicked.connect(self.press_third_btn8_3_1)
        self.btn_2.clicked.connect(self.press_third_btn8_3_2)
        self.btn_7.clicked.connect(self.press_third_btn8_3_7)
        self.btn_9.clicked.connect(self.press_third_btn8_3_9)
        self.btn_4.clicked.connect(self.press_third_btn8_3_4)


        self.btn_2.clicked.connect(self.press_third_btn8_4_2)
        self.btn_3.clicked.connect(self.press_third_btn8_4_3)
        self.btn_6.clicked.connect(self.press_third_btn8_4_6)
        self.btn_7.clicked.connect(self.press_third_btn8_4_7)
        self.btn_1.clicked.connect(self.press_third_btn8_4_1)


        self.btn_1.clicked.connect(self.press_third_btn8_6_1)
        self.btn_2.clicked.connect(self.press_third_btn8_6_2)
        self.btn_4.clicked.connect(self.press_third_btn8_6_4)
        self.btn_9.clicked.connect(self.press_third_btn8_6_9)
        self.btn_3.clicked.connect(self.press_third_btn8_6_3)


        self.btn_2.clicked.connect(self.press_third_btn8_7_2)
        self.btn_3.clicked.connect(self.press_third_btn8_7_3)
        self.btn_4.clicked.connect(self.press_third_btn8_7_4)
        self.btn_6.clicked.connect(self.press_third_btn8_7_6)
        self.btn_1.clicked.connect(self.press_third_btn8_7_1)


        self.btn_1.clicked.connect(self.press_third_btn8_9_1)
        self.btn_2.clicked.connect(self.press_third_btn8_9_2)
        self.btn_4.clicked.connect(self.press_third_btn8_9_4)
        self.btn_6.clicked.connect(self.press_third_btn9_8_6)
        self.btn_3.clicked.connect(self.press_third_btn8_9_3)


        self.btn_3.clicked.connect(self.press_third_btn9_1_3)
        self.btn_4.clicked.connect(self.press_third_btn9_1_4)
        self.btn_6.clicked.connect(self.press_third_btn9_1_6)
        self.btn_7.clicked.connect(self.press_third_btn9_1_7)
        self.btn_8.clicked.connect(self.press_third_btn9_1_8)


        self.btn_1.clicked.connect(self.press_third_btn9_2_1)
        self.btn_3.clicked.connect(self.press_third_btn9_2_3)
        self.btn_7.clicked.connect(self.press_third_btn9_2_7)
        self.btn_8.clicked.connect(self.press_third_btn9_2_8)
        self.btn_4.clicked.connect(self.press_third_btn9_2_4)


        self.btn_1.clicked.connect(self.press_third_btn9_3_1)
        self.btn_2.clicked.connect(self.press_third_btn9_3_2)
        self.btn_7.clicked.connect(self.press_third_btn9_3_7)
        self.btn_8.clicked.connect(self.press_third_btn9_3_8)
        self.btn_4.clicked.connect(self.press_third_btn9_3_4)

        self.btn_1.clicked.connect(self.press_third_btn9_4_1)
        self.btn_3.clicked.connect(self.press_third_btn9_4_3)
        self.btn_6.clicked.connect(self.press_third_btn9_4_6)
        self.btn_7.clicked.connect(self.press_third_btn9_4_7)
        self.btn_2.clicked.connect(self.press_third_btn9_4_2)


        self.btn_1.clicked.connect(self.press_third_btn9_6_1)
        self.btn_2.clicked.connect(self.press_third_btn9_6_2)
        self.btn_4.clicked.connect(self.press_third_btn9_6_4)
        self.btn_8.clicked.connect(self.press_third_btn9_6_8)
        self.btn_7.clicked.connect(self.press_third_btn9_6_7)


        self.btn_1.clicked.connect(self.press_third_btn9_7_1)
        self.btn_3.clicked.connect(self.press_third_btn9_7_3)
        self.btn_4.clicked.connect(self.press_third_btn9_7_4)
        self.btn_6.clicked.connect(self.press_third_btn9_7_6)
        self.btn_2.clicked.connect(self.press_third_btn9_7_2)

    
        self.btn_1.clicked.connect(self.press_third_btn9_8_1)
        self.btn_2.clicked.connect(self.press_third_btn9_8_2)
        self.btn_4.clicked.connect(self.press_third_btn9_8_4)
        self.btn_6.clicked.connect(self.press_third_btn9_8_6)
        self.btn_3.clicked.connect(self.press_third_btn9_8_3)



        self.btn_6.clicked.connect(self.press_four_btn1_2_7_6)
        self.btn_8.clicked.connect(self.press_four_btn1_2_7_8)
        self.btn_9.clicked.connect(self.press_four_btn1_2_7_9)


        self.btn_9.clicked.connect(self.press_four_btn1_3_8_9)
        self.btn_7.clicked.connect(self.press_four_btn1_3_8_7)
        self.btn_4.clicked.connect(self.press_four_btn1_3_8_4)


        self.btn_6.clicked.connect(self.press_four_btn1_4_3_6)
        self.btn_9.clicked.connect(self.press_four_btn1_4_3_9)
        self.btn_8.clicked.connect(self.press_four_btn1_4_3_8)


        self.btn_4.clicked.connect(self.press_four_btn1_6_8_4)
        self.btn_9.clicked.connect(self.press_four_btn1_6_8_9)
        self.btn_3.clicked.connect(self.press_four_btn1_6_8_3)


        self.btn_3.clicked.connect(self.press_four_btn1_7_6_3)
        self.btn_9.clicked.connect(self.press_four_btn1_7_6_9)
        self.btn_2.clicked.connect(self.press_four_btn1_7_6_2)


        self.btn_2.clicked.connect(self.press_four_btn1_8_6_2)
        self.btn_9.clicked.connect(self.press_four_btn1_8_6_9)
        self.btn_7.clicked.connect(self.press_four_btn1_8_6_7)


        self.btn_4.clicked.connect(self.press_four_btn1_9_8_4)
        self.btn_6.clicked.connect(self.press_four_btn1_9_8_6)
        self.btn_3.clicked.connect(self.press_four_btn1_9_8_3)


        self.btn_8.clicked.connect(self.press_four_btn2_3_9_8)
        self.btn_7.clicked.connect(self.press_four_btn2_3_9_7)
        self.btn_4.clicked.connect(self.press_four_btn2_3_9_4)


        self.btn_8.clicked.connect(self.press_four_btn2_4_7_8)
        self.btn_6.clicked.connect(self.press_four_btn2_4_7_6)
        self.btn_9.clicked.connect(self.press_four_btn2_4_7_9)


        self.btn_8.clicked.connect(self.press_four_btn2_6_9_8)
        self.btn_4.clicked.connect(self.press_four_btn2_6_9_4)
        self.btn_7.clicked.connect(self.press_four_btn2_6_9_7)


        self.btn_3.clicked.connect(self.press_four_btn2_7_6_3)
        self.btn_8.clicked.connect(self.press_four_btn2_7_6_8)
        self.btn_1.clicked.connect(self.press_four_btn2_7_6_1)


        self.btn_4.clicked.connect(self.press_four_btn2_8_3_4)
        self.btn_6.clicked.connect(self.press_four_btn2_8_3_6)
        self.btn_9.clicked.connect(self.press_four_btn2_8_3_9)


        self.btn_1.clicked.connect(self.press_four_btn2_9_4_1)
        self.btn_8.clicked.connect(self.press_four_btn2_9_4_8)
        self.btn_3.clicked.connect(self.press_four_btn2_9_4_3)


        self.btn_6.clicked.connect(self.press_four_btn3_4_8_6)
        self.btn_7.clicked.connect(self.press_four_btn3_4_8_7)
        self.btn_1.clicked.connect(self.press_four_btn3_4_8_1)


        self.btn_4.clicked.connect(self.press_four_btn3_6_1_4)
        self.btn_7.clicked.connect(self.press_four_btn3_6_1_7)
        self.btn_8.clicked.connect(self.press_four_btn3_6_1_8)


        self.btn_4.clicked.connect(self.press_four_btn3_7_8_4)
        self.btn_6.clicked.connect(self.press_four_btn3_7_8_6)
        self.btn_1.clicked.connect(self.press_four_btn3_7_8_1)


        self.btn_2.clicked.connect(self.press_four_btn3_8_4_2)
        self.btn_7.clicked.connect(self.press_four_btn3_8_4_7)
        self.btn_9.clicked.connect(self.press_four_btn3_8_4_9)


        self.btn_1.clicked.connect(self.press_four_btn3_9_4_1)
        self.btn_7.clicked.connect(self.press_four_btn3_9_4_7)
        self.btn_2.clicked.connect(self.press_four_btn3_9_4_2)


        self.btn_6.clicked.connect(self.press_four_btn4_1_3_6)
        self.btn_9.clicked.connect(self.press_four_btn4_1_3_9)
        self.btn_8.clicked.connect(self.press_four_btn4_1_3_8)


        self.btn_6.clicked.connect(self.press_four_btn4_2_7_6)
        self.btn_8.clicked.connect(self.press_four_btn4_2_7_8)
        self.btn_9.clicked.connect(self.press_four_btn4_2_7_9)


        self.btn_6.clicked.connect(self.press_four_btn4_3_8_6)
        self.btn_7.clicked.connect(self.press_four_btn4_3_8_7)
        self.btn_1.clicked.connect(self.press_four_btn4_3_8_1)


        self.btn_2.clicked.connect(self.press_four_btn4_6_7_2)
        self.btn_8.clicked.connect(self.press_four_btn4_6_7_8)
        self.btn_9.clicked.connect(self.press_four_btn4_6_7_9)


        self.btn_6.clicked.connect(self.press_four_btn4_7_9_6)
        self.btn_3.clicked.connect(self.press_four_btn4_7_9_3)
        self.btn_2.clicked.connect(self.press_four_btn4_7_9_2)


        self.btn_2.clicked.connect(self.press_four_btn4_8_1_2)
        self.btn_6.clicked.connect(self.press_four_btn4_8_1_6)
        self.btn_3.clicked.connect(self.press_four_btn4_8_1_3)


        self.btn_1.clicked.connect(self.press_four_btn4_9_2_1)
        self.btn_6.clicked.connect(self.press_four_btn4_9_2_6)
        self.btn_7.clicked.connect(self.press_four_btn4_9_2_7)       


        self.btn_4.clicked.connect(self.press_four_btn5_2_3_4)
        self.btn_9.clicked.connect(self.press_four_btn5_2_3_9)
        self.btn_6.clicked.connect(self.press_four_btn5_2_3_6)   


        self.btn_3.clicked.connect(self.press_four_btn5_2_4_3)
        self.btn_7.clicked.connect(self.press_four_btn5_2_4_7)
        self.btn_9.clicked.connect(self.press_four_btn5_2_4_9)  


        self.btn_7.clicked.connect(self.press_four_btn5_2_6_7)
        self.btn_3.clicked.connect(self.press_four_btn5_2_6_3)
        self.btn_9.clicked.connect(self.press_four_btn5_2_6_9)  


        self.btn_4.clicked.connect(self.press_four_btn5_2_7_4)
        self.btn_6.clicked.connect(self.press_four_btn5_2_7_6)
        self.btn_9.clicked.connect(self.press_four_btn5_2_7_9)  


        self.btn_4.clicked.connect(self.press_four_btn5_2_9_4)
        self.btn_6.clicked.connect(self.press_four_btn5_2_9_6)
        self.btn_7.clicked.connect(self.press_four_btn5_2_9_7)  


        self.btn_2.clicked.connect(self.press_four_btn5_3_4_2)
        self.btn_8.clicked.connect(self.press_four_btn5_3_4_8)
        self.btn_9.clicked.connect(self.press_four_btn5_3_4_9)   


        self.btn_3.clicked.connect(self.press_four_btn5_4_2_3)
        self.btn_7.clicked.connect(self.press_four_btn5_4_2_7)
        self.btn_9.clicked.connect(self.press_four_btn5_4_2_9)   


        self.btn_2.clicked.connect(self.press_four_btn5_6_7_2)
        self.btn_8.clicked.connect(self.press_four_btn5_6_7_8)
        self.btn_9.clicked.connect(self.press_four_btn5_6_7_9)   


        self.btn_6.clicked.connect(self.press_four_btn5_8_3_6)
        self.btn_9.clicked.connect(self.press_four_btn5_8_3_9)
        self.btn_4.clicked.connect(self.press_four_btn5_8_3_4)   


        self.btn_3.clicked.connect(self.press_four_btn6_7_2_3)
        self.btn_4.clicked.connect(self.press_four_btn6_7_2_4)
        self.btn_9.clicked.connect(self.press_four_btn6_7_2_9)  


        self.btn_2.clicked.connect(self.press_four_btn6_8_3_2)
        self.btn_4.clicked.connect(self.press_four_btn6_8_3_4)
        self.btn_1.clicked.connect(self.press_four_btn6_8_3_1)  


        self.btn_1.clicked.connect(self.press_four_btn6_9_7_1)
        self.btn_4.clicked.connect(self.press_four_btn6_9_7_4)
        self.btn_2.clicked.connect(self.press_four_btn6_9_7_2) 


        self.btn_9.clicked.connect(self.press_four_btn7_1_6_9)
        self.btn_3.clicked.connect(self.press_four_btn7_1_6_3)
        self.btn_2.clicked.connect(self.press_four_btn7_1_6_2) 


        self.btn_2.clicked.connect(self.press_four_btn7_8_1_2)
        self.btn_3.clicked.connect(self.press_four_btn7_8_1_3)
        self.btn_6.clicked.connect(self.press_four_btn7_8_1_6) 


        self.btn_1.clicked.connect(self.press_four_btn7_9_2_1)
        self.btn_3.clicked.connect(self.press_four_btn7_9_2_3)
        self.btn_4.clicked.connect(self.press_four_btn7_9_2_4) 


        self.btn_9.clicked.connect(self.press_four_btn8_2_3_9) 


        self.btn_1.clicked.connect(self.press_four_btn8_9_3_1)
        self.btn_2.clicked.connect(self.press_four_btn8_9_3_2)
        self.btn_4.clicked.connect(self.press_four_btn8_9_3_4) 

        self.btn_try_agin.clicked.connect(self.press_btn_try_agin)


            

    def press_btn1(self):
        if self.list.count('1') == 0 : 
            self.btn_1.setText('X')
            self.btn_1.setStyleSheet("color : 		#FF0000 ")
            self.list.append('1') 
    
    def press_btn2(self):
        if self.list.count('2') == 0 : 
            self.btn_2.setText('X')
            self.btn_2.setStyleSheet("color : 		#FF0000")
            self.list.append('2')

    def press_btn3(self):
        if self.list.count('3') == 0 : 
            self.btn_3.setText('X')
            self.btn_3.setStyleSheet("color : 	#FF0000 ")
            self.list.append('3')

    def press_btn4(self):
        if self.list.count('4') == 0 : 
            self.btn_4.setText('X')
            self.btn_4.setStyleSheet("color : 		#FF0000 ")
            self.list.append('4')

    def press_btn5(self):
        if self.list.count('5') == 0:
            self.btn_5.setText('X')
            self.btn_5.setStyleSheet("color : 		#FF0000")
            self.list.append('5')
            print('Creator by Sanjarbek')


    def press_btn6(self):
        if self.list.count('6') == 0 : 
            self.btn_6.setText('X')
            self.btn_6.setStyleSheet("color : 		#FF0000")
            self.list.append('6')


    def press_btn7(self):
        if self.list.count('7') == 0 : 
            self.btn_7.setText('X')
            self.btn_7.setStyleSheet("color : 		#FF0000 ")
            self.list.append('7')


    def press_btn8(self):
        if self.list.count('8') == 0 : 
            self.btn_8.setText('X')
            self.btn_8.setStyleSheet("color : 		#FF0000")
            self.list.append('8')


    def press_btn9(self):
        if self.list.count('9') == 0 : 
            self.btn_9.setText('X')
            self.btn_9.setStyleSheet("color : 	#FF0000 ")
            self.list.append('9')


    # SUNIY INTELECT 

    def press_first_btn1(self):
        if self.list.count('5') == 0 and  len(self.list) == 1 :
            self.btn_5.setText('O')
            self.count += 1
            
            self.winner.append('5')
    
    def press_first_btn2(self):
        if self.list.count('5') == 0 and  len(self.list) == 1 :
            self.btn_5.setText('O')
            self.count += 1

            self.winner.append('5')

            # self.counter2.append('1')


    def press_first_btn3(self):
        if self.list.count('5') == 0 and  len(self.list) == 1 :
            self.btn_5.setText('O')
            self.count += 1
            # self.counter3.append('1')

            self.winner.append('5')

    
    def press_first_btn4(self):
        if self.list.count('5') == 0 and  len(self.list) == 1 :
            self.btn_5.setText('O')
            self.count += 1
            # self.counter4.append('1')

            self.winner.append('5')


    def press_first_btn5(self):
        if self.list.count('1') == 0 and  len(self.list) == 1 :
            self.btn_1.setText('O')
            self.count += 1
            # self.counter5.append('1')

            self.winner.append('1')


    def press_first_btn6(self):
        if self.list.count('5') == 0 and  len(self.list) == 1:
            self.btn_5.setText('O')
            self.count += 1
            # self.counter6.append('1')

            self.winner.append('5')


    def press_first_btn7(self):
        if self.list.count('5') == 0 and  len(self.list) == 1:
            self.btn_5.setText('O')
            self.count += 1
            # self.counter7.append('1')

            self.winner.append('5')


    def press_first_btn8(self):
        if self.list.count('5') == 0 and  len(self.list) == 1:
            self.btn_5.setText('O')
            self.count += 1
            # self.counter8.append('1')

            self.winner.append('5')

        
    def press_first_btn9(self):
        if self.list.count('5') == 0 and  len(self.list) == 1:
            self.btn_5.setText('O')
            self.count += 1
            # self.counter9.append('1')

            self.winner.append('5')

    # SECOND BUTTON 5 AND ...

    def press_second_btn5_2(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and len(self.list) == 2:
            self.btn_8.setText('O')

            self.winner.append('8')
        
    def press_second_btn5_3(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')
        
    def press_second_btn5_4(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and  len(self.list) == 2: 
            self.btn_6.setText('O')

            self.winner.append('6')

    def press_second_btn5_6(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')

            self.winner.append('4')
        
    def press_second_btn5_7(self):
        if self.list.count('5') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')
        
    def press_second_btn5_8(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')
        
    def press_second_btn5_9(self):
        if self.list.count('5') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')

    

    def press_second1_3(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')


    def press_second1_2(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_second1_4(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')
        
    def press_second1_6(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')
        
    def press_second1_7(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')

            self.winner.append('4')

    def press_second1_8(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')

            self.winner.append('4')
        
    def press_second1_9(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')




    def press_btn2_1(self):
        if self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')
        
    def press_btn2_3(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_btn2_4(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_btn2_6(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_btn2_7(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_btn2_8(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_btn2_9(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_6.setText('O')

            self.winner.append('7')

    
    def press_btn3_1(self):
        if self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')

    def press_btn3_2(self):
        if self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_btn3_4(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')

    def press_btn3_6(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_9.setText('O')

            self.winner.append('9')

    def press_btn3_7(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')

    def press_btn3_8(self):
        if self.list.count('3') == 1  and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_6.setText('O')

            self.winner.append('6')

    def press_btn3_9(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_6.setText('O')

            self.winner.append('6')



    def press_btn4_1(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_btn4_2(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')

    def press_btn4_3(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')
    
    def press_btn4_6(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_btn4_7(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_btn4_8(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_9.setText('O')

            self.winner.append('9')

    def press_btn4_9(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_8.setText('O')

            self.winner.append('8')




    def press_btn6_1(self):
        if self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')

    def press_btn6_2(self):
        if self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_1.setText('O')

            self.winner.append('1')

    def press_btn6_3(self):
        if self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_9.setText('O')

            self.winner.append('9')



    def press_btn6_4(self):
        if self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')
            
            self.winner.append('3')

    def press_btn6_7(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_btn6_8(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_btn6_9(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')
            self.winner.append('3')
 


    def press_btn7_1(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')

            self.winner.append('4')

    def press_btn7_2(self):
        if self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_btn7_3(self):
        if self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_btn7_4(self):
        if self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_btn7_6(self):
        if self.list.count('7') == 1 and self.list.count('6') ==  1 and  len(self.list) == 2:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_btn7_8(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_btn7_9(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_8.setText('O')
            self.winner.append('8')

    

    def press_btn8_1(self):
        if self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_btn8_2(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')

    def press_btn8_3(self):
        if self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_6.setText('O')

            self.winner.append('6')

    def press_btn8_4(self):
        if self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_9.setText('O')

            self.winner.append('9')

    def press_btn8_6(self):
        if self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')

    def press_btn8_7(self):
        if self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_btn8_9(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')
            self.winner.append('7')




    def press_btn9_1(self):
        if self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 2:
            self.btn_2.setText('O')

            self.winner.append('2')

    def press_btn9_2(self):
        if self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 2:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_btn9_3(self):
        if self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 2:
            self.btn_6.setText('O')

            self.winner.append('6')

    def press_btn9_4(self):
        if self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 2:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_btn9_6(self):
        if self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 2:
            self.btn_3.setText('O')

            self.winner.append('3')

    def press_btn9_7(self):
        if self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 2:

            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_btn9_8(self):
        if self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 2:
            self.btn_7.setText('O')

            self.winner.append('7')

    


    def press_third_btn1_2_4(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn1_2_6(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn1_2_8(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn1_2_9(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn1_2_7(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')





    def press_third_btn1_3_4(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn1_3_6(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn1_3_7(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn1_3_9(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn1_3_8(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')




    def press_third_btn1_4_2(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')

            self.winner.append('3')
    
    def press_third_btn1_4_6(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn1_4_8(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn1_4_9(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn1_4_3(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')

            self.winner.append('2')



    def press_third_btn1_6_3(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_6_4(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_6_7(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_6_9(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_6_8(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')


    def press_third_btn1_7_2(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_7_3(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_7_8(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_7_9(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_7_6(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')



    def press_third_btn1_8_2(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_8_3(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_8_7(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_8_9(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn1_8_6(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    


    def press_third_btn1_9_3(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_9_4(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_9_6(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_9_7(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn1_9_8(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
     
    
    def press_third_btn2_1_4(self):
        if self.list.count('2') == 1 and self.list.count('1') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_1_6(self):
        if self.list.count('2') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_1_8(self):
        if self.list.count('2') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_1_9(self):
        if self.list.count('2') == 1 and self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_1_7(self):
        if self.list.count('2') == 1 and self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')


    def press_third_btn2_3_4(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn2_3_6(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn2_3_7(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn2_3_8(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn2_3_9(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    


    def press_third_btn2_4_1(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_4_6(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_4_8(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_4_9(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn2_4_7(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    


    def press_third_btn2_6_3(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn2_6_4(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn2_6_7(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn2_6_8(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn2_6_9(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_third_btn2_7_1(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn2_7_3(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn2_7_8(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn2_7_9(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn2_7_6(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')


    def press_third_btn2_8_1(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn2_8_4(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn2_8_6(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn2_8_9(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn2_8_3(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')



    def press_third_btn2_9_1(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn2_9_3(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn2_9_7(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn2_9_8(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn2_9_4(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')



    def press_third_btn3_1_4(self):
        if self.list.count('3') == 1 and self.list.count('1') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn3_1_6(self):
        if self.list.count('3') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn3_1_7(self):
        if self.list.count('3') == 1 and self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn3_1_9(self):
        if self.list.count('3') == 1 and self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_1_8(self):
        if self.list.count('3') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')



    def press_third_btn3_2_4(self):
        if self.list.count('3') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn3_2_6(self):
        if self.list.count('3') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn3_2_7(self):
        if self.list.count('3') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn3_2_8(self):
        if self.list.count('3') == 1 and self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn3_2_9(self):
        if self.list.count('3') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')



    def press_third_btn3_4_1(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_4_6(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_4_7(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_4_9(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_4_8(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')



    def press_third_btn3_6_2(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn3_6_4(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn3_6_7(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn3_6_8(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn3_6_1(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')

            self.winner.append('2')


    def press_third_btn3_7_1(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_7_4(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_7_6(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_7_9(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn3_7_8(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')


    def press_third_btn3_8_1(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_8_2(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_8_7(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_8_9(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_8_4(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')


    def press_third_btn3_9_1(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_9_2(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_9_7(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_9_8(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn3_9_4(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')



    def press_third_btn4_1_2(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn4_1_6(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn4_1_8(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 

            self.winner.append('3')
    
    def press_third_btn4_1_9(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn4_1_3(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')

            self.winner.append('2')


    def press_third_btn4_2_1(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn4_2_6(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn4_2_8(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O') 

            self.winner.append('7')
    
    def press_third_btn4_2_9(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn4_2_7(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')



    def press_third_btn4_3_1(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn4_3_6(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn4_3_7(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O') 

            self.winner.append('8')
    
    def press_third_btn4_3_9(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')
    
    def press_third_btn4_3_8(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('4')


    def press_third_btn4_6_1(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('4')
    
    def press_third_btn4_6_2(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn4_6_8(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O') 

            self.winner.append('7')
    
    def press_third_btn4_6_9(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn4_6_7(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')



    def press_third_btn4_7_2(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn4_7_3(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn4_7_6(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O') 

            self.winner.append('9')
    
    def press_third_btn4_7_8(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')

            self.winner.append('9')
    
    def press_third_btn4_7_9(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')

            self.winner.append('8')


    def press_third_btn4_8_2(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn4_8_3(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn4_8_6(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O') 

            self.winner.append('1')
    
    def press_third_btn4_8_7(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')

            self.winner.append('1')
    
    def press_third_btn4_8_1(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    


    def press_third_btn4_9_1(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')

            self.winner.append('2')
    
    def press_third_btn4_9_3(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')

            self.winner.append('2')
    
    def press_third_btn4_9_6(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O') 

            self.winner.append('2')
    
    def press_third_btn4_9_7(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')

            self.winner.append('2')
    
    def press_third_btn4_9_2(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')


    def press_third_btn5_2_3(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')

            self.winner.append('7')
    
    def press_third_btn5_2_4(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn5_2_7(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 

            self.winner.append('3')
    
    def press_third_btn5_2_9(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')

            self.winner.append('3')
    
    def press_third_btn5_2_6(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')


    def press_third_btn5_3_2(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn5_3_4(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')

            self.winner.append('6')
    
    def press_third_btn5_3_6(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4') 
    
    def press_third_btn5_3_8(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn5_3_9(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')



    def press_third_btn5_4_2(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn5_4_3(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn5_4_7(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn5_4_8(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_4_9(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')



    def press_third_btn5_6_2(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn5_6_3(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn5_6_8(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O') 
            self.winner.append('7')
    
    def press_third_btn5_6_9(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn5_6_7(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_third_btn5_7_4(self):
        if self.list.count('5') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_7_6(self):
        if self.list.count('5') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_7_8(self):
        if self.list.count('5') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O') 
            self.winner.append('2')
    
    def press_third_btn5_7_9(self):
        if self.list.count('5') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_7_2(self):
        if self.list.count('5') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')


    def press_third_btn5_8_4(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn5_8_6(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('')
    
    def press_third_btn5_8_7(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn5_8_9(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn5_8_3(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')



    def press_third_btn5_9_4(self):
        if self.list.count('5') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_9_6(self):
        if self.list.count('5') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_9_7(self):
        if self.list.count('5') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2') 
    
    def press_third_btn5_9_8(self):
        if self.list.count('5') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn5_9_2(self):
        if self.list.count('5') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')


    def press_third_btn6_1_3(self):
        if self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn6_1_4(self):
        if self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn6_1_7(self):
        if self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O') 
            self.winner.append('8')
    
    def press_third_btn6_1_9(self):
        if self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn6_1_8(self):
        if self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')



    def press_third_btn6_2_3(self):
        if self.list.count('6') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn6_2_4(self):
        if self.list.count('6') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn6_2_7(self):
        if self.list.count('6') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O') 
            self.winner.append('9')
    
    def press_third_btn6_2_8(self):
        if self.list.count('6') == 1 and self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn6_2_9(self):
        if self.list.count('6') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_third_btn6_3_2(self):
        if self.list.count('6') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn6_3_4(self):
        if self.list.count('6') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn6_3_7(self):
        if self.list.count('6') == 1 and self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O') 
            self.winner.append('1')
    
    def press_third_btn6_3_8(self):
        if self.list.count('6') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn6_3_1(self):
        if self.list.count('6') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')


    def press_third_btn6_4_1(self):
        if self.list.count('6') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn6_4_2(self):
        if self.list.count('6') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn6_4_8(self):
        if self.list.count('6') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O') 
            self.winner.append('7')
    
    def press_third_btn6_4_9(self):
        if self.list.count('6') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn6_4_7(self):
        if self.list.count('6') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')



    def press_third_btn6_7_1(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn6_7_3(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn6_7_4(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O') 
            self.winner.append('2')
    
    def press_third_btn6_7_9(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn6_7_2(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')


    def press_third_btn6_8_1(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn6_8_2(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn6_8_4(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn6_8_9(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn6_8_3(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')



    def press_third_btn6_9_1(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn6_9_2(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn6_9_4(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O') 
            self.winner.append('7')
    
    def press_third_btn6_9_8(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn6_9_7(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')


    def press_third_btn7_1_2(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn7_1_3(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn7_1_8(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6') 
    
    def press_third_btn7_1_9(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn7_1_6(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')



    def press_third_btn7_2_1(self):
        if self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn7_2_3(self):
        if self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn7_2_8(self):
        if self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O') 
            self.winner.append('6')
    
    def press_third_btn7_2_9(self):
        if self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn7_2_6(self):
        if self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')



    def press_third_btn7_3_1(self):
        if self.list.count('7') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn7_3_4(self):
        if self.list.count('7') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn7_3_6(self):
        if self.list.count('7') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O') 
            self.winner.append('8')
    
    def press_third_btn7_3_9(self):
        if self.list.count('7') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn7_3_8(self):
        if self.list.count('7') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')



    def press_third_btn7_4_2(self):
        if self.list.count('7') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn7_4_6(self):
        if self.list.count('7') == 1 and self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn7_4_3(self):
        if self.list.count('7') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O') 
            self.winner.append('9')
    
    def press_third_btn7_4_8(self):
        if self.list.count('7') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')
    
    def press_third_btn7_4_9(self):
        if self.list.count('7') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')



    def press_third_btn7_6_1(self):
        if self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn7_6_3(self):
        if self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn7_6_4(self):
        if self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O') 
            self.winner.append('2')
    
    def press_third_btn7_6_9(self):
        if self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn7_6_2(self):
        if self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')



    def press_third_btn7_8_2(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn7_8_3(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn7_8_4(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O') 
            self.winner.append('1')
    
    def press_third_btn7_8_6(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn7_8_1(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')


    def press_third_btn7_9_1(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn7_9_3(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn7_9_4(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2') 
    
    def press_third_btn7_9_6(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn7_9_2(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')


    def press_third_btn8_1_2(self):
        if self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn8_1_3(self):
        if self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn8_1_7(self):
        if self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O') 
            self.winner.append('6')
    
    def press_third_btn8_1_9(self):
        if self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')
    
    def press_third_btn8_1_6(self):
        if self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_third_btn8_2_1(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_2_4(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_2_6(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn8_2_9(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_2_3(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')


    def press_third_btn8_3_1(self):
        if self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn8_3_2(self):
        if self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn8_3_7(self):
        if self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O') 
            self.winner.append('4')
    
    def press_third_btn8_3_9(self):
        if self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn8_3_4(self):
        if self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')



    def press_third_btn8_4_2(self):
        if self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn8_4_3(self):
        if self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn8_4_6(self):
        if self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O') 
            self.winner.append('1')
    
    def press_third_btn8_4_7(self):
        if self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn8_4_1(self):
        if self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')


    def press_third_btn8_6_1(self):
        if self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_6_2(self):
        if self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_6_4(self):
        if self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn8_6_9(self):
        if self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_6_3(self):
        if self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_9.setText('O')
            self.winner.append('9')


    def press_third_btn8_7_2(self):
        if self.list.count('8') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn8_7_3(self):
        if self.list.count('8') == 1 and self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn8_7_4(self):
        if self.list.count('8') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O') 
            self.winner.append('1')
    
    def press_third_btn8_7_6(self):
        if self.list.count('8') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_1.setText('O')
            self.winner.append('1')
    
    def press_third_btn8_7_1(self):
        if self.list.count('8') == 1 and self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')


    def press_third_btn8_9_1(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_9_2(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_9_4(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn9_8_6(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn8_9_3(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')


    def press_third_btn9_1_3(self):
        if self.list.count('9') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn9_1_4(self):
        if self.list.count('9') == 1 and self.list.count('1') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn9_1_6(self):
        if self.list.count('9') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O') 
            self.winner.append('8')
    
    def press_third_btn9_1_7(self):
        if self.list.count('9') == 1 and self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')
    
    def press_third_btn9_1_8(self):
        if self.list.count('9') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')


    def press_third_btn9_2_1(self):
        if self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')

            self.winner.append('4')
    
    def press_third_btn9_2_3(self):
        if self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn9_2_7(self):
        if self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O') 
            self.winner.append('4')
    
    def press_third_btn9_2_8(self):
        if self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn9_2_4(self):
        if self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')


    def press_third_btn9_3_1(self):
        if self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn9_3_2(self):
        if self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn9_3_7(self):
        if self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O') 
            self.winner.append('4')
    
    def press_third_btn9_3_8(self):
        if self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_4.setText('O')
            self.winner.append('4')
    
    def press_third_btn9_3_4(self):
        if self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')


    def press_third_btn9_4_1(self):
        if self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn9_4_3(self):
        if self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn9_4_6(self):
        if self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O') 
            self.winner.append('2')
    
    def press_third_btn9_4_7(self):
        if self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn9_4_2(self):
        if self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_third_btn9_6_1(self):
        if self.list.count('9') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn9_6_2(self):
        if self.list.count('9') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn9_6_4(self):
        if self.list.count('9') == 1 and self.list.count('6') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O') 
            self.winner.append('7')
    
    def press_third_btn9_6_8(self):
        if self.list.count('9') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 3:
            self.btn_7.setText('O')
            self.winner.append('7')
    
    def press_third_btn9_6_7(self):
        if self.list.count('9') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 3:
            self.btn_8.setText('O')
            self.winner.append('8')



    def press_third_btn9_7_1(self):
        if self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn9_7_3(self):
        if self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn9_7_4(self):
        if self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O') 
            self.winner.append('2')
    
    def press_third_btn9_7_6(self):
        if self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_2.setText('O')
            self.winner.append('2')
    
    def press_third_btn9_7_2(self):
        if self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')



    def press_third_btn9_8_1(self):
        if self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn9_8_2(self):
        if self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('2') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn9_8_4(self):
        if self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O') 
            self.winner.append('3')
    
    def press_third_btn9_8_6(self):
        if self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 3:
            self.btn_3.setText('O')
            self.winner.append('3')
    
    def press_third_btn9_8_3(self):
        if self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 3:
            self.btn_6.setText('O')
            self.winner.append('6')





    def press_four_btn1_2_7_6(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn1_2_7_8(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')

    def press_four_btn1_2_7_9(self):
        if self.list.count('1') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')



    def press_four_btn1_3_8_9(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn1_3_8_7(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn1_3_8_4(self):
        if self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    

    def press_four_btn1_4_3_6(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_four_btn1_4_3_9(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_four_btn1_4_3_8(self):
        if self.list.count('1') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')



    def press_four_btn1_6_8_4(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn1_6_8_9(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn1_6_8_3(self):
        if self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    

    def press_four_btn1_7_6_3(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn1_7_6_9(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn1_7_6_2(self):
        if self.list.count('1') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')


    def press_four_btn1_8_6_2(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_four_btn1_8_6_9(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_four_btn1_8_6_7(self):
        if self.list.count('1') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')


    def press_four_btn1_9_8_4(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn1_9_8_6(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn1_9_8_3(self):
        if self.list.count('1') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')



    def press_four_btn2_3_9_8(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn2_3_9_7(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn2_3_9_4(self):
        if self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')



    def press_four_btn2_4_7_8(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn2_4_7_6(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn2_4_7_9(self):
        if self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')



    def press_four_btn2_6_9_8(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_four_btn2_6_9_4(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_four_btn2_6_9_7(self):
        if self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')



    def press_four_btn2_7_6_3(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn2_7_6_8(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn2_7_6_1(self):
        if self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn2_8_3_4(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn2_8_3_6(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn2_8_3_9(self):
        if self.list.count('2') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')



    def press_four_btn2_9_4_1(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn2_9_4_8(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn2_9_4_3(self):
        if self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')


    def press_four_btn3_4_8_6(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn3_4_8_7(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn3_4_8_1(self):
        if self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')
            


    def press_four_btn3_6_1_4(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_four_btn3_6_1_7(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_four_btn3_6_1_8(self):
        if self.list.count('3') == 1 and self.list.count('6') == 1 and self.list.count('1') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')


    def press_four_btn3_7_8_4(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn3_7_8_6(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn3_7_8_1(self):
        if self.list.count('3') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')


    def press_four_btn3_8_4_2(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn3_8_4_7(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn3_8_4_9(self):
        if self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')


    def press_four_btn3_9_4_1(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn3_9_4_7(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn3_9_4_2(self):
        if self.list.count('3') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')


    def press_four_btn4_1_3_6(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_four_btn4_1_3_9(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')

    def press_four_btn4_1_3_8(self):
        if self.list.count('4') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')



    def press_four_btn4_2_7_6(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn4_2_7_8(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn4_2_7_9(self):
        if self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')


    def press_four_btn4_3_8_6(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn4_3_8_7(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn4_3_8_1(self):
        if self.list.count('4') == 1 and self.list.count('3') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')


    def press_four_btn4_6_7_2(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn4_6_7_8(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn4_6_7_9(self):
        if self.list.count('4') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')


    def press_four_btn4_7_9_6(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn4_7_9_3(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn4_7_9_2(self):
        if self.list.count('4') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn4_8_1_2(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn4_8_1_6(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn4_8_1_3(self):
        if self.list.count('4') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')




    def press_four_btn4_9_2_1(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')
            

    def press_four_btn4_9_2_6(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_four_btn4_9_2_7(self):
        if self.list.count('4') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')




    def press_four_btn5_2_3_4(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')
            
    def press_four_btn5_2_3_9(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn5_2_3_6(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')



    def press_four_btn5_2_4_3(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')
            
    def press_four_btn5_2_4_7(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn5_2_4_9(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn5_2_6_7(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')
            
    def press_four_btn5_2_6_3(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    def press_four_btn5_2_6_9(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')

    

    def press_four_btn5_2_7_4(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')
            
    def press_four_btn5_2_7_6(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn5_2_7_9(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')


    def press_four_btn5_2_9_4(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')
            
    def press_four_btn5_2_9_6(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn5_2_9_7(self):
        if self.list.count('5') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')



    def press_four_btn5_3_4_2(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')
            
    def press_four_btn5_3_4_8(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn5_3_4_9(self):
        if self.list.count('5') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')


    def press_four_btn5_4_2_3(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_7.setText('O')
            self.winner.append('7')
            
    def press_four_btn5_4_2_7(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('7') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')

    def press_four_btn5_4_2_9(self):
        if self.list.count('5') == 1 and self.list.count('4') == 1 and self.list.count('2') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn5_6_7_2(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')
            
    def press_four_btn5_6_7_8(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn5_6_7_9(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')


    def press_four_btn5_6_7_2(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_8.setText('O')
            self.winner.append('8')
            
    def press_four_btn5_6_7_8(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('8') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')

    def press_four_btn5_6_7_9(self):
        if self.list.count('5') == 1 and self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')


    def press_four_btn5_8_3_6(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')
            
    def press_four_btn5_8_3_9(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn5_8_3_4(self):
        if self.list.count('5') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')


    def press_four_btn6_7_2_3(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')
            
    def press_four_btn6_7_2_4(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_9.setText('O')
            self.winner.append('9')

    def press_four_btn6_7_2_9(self):
        if self.list.count('6') == 1 and self.list.count('7') == 1 and self.list.count('7') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn6_8_3_2(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')
            
    def press_four_btn6_8_3_4(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')

    def press_four_btn6_8_3_1(self):
        if self.list.count('6') == 1 and self.list.count('8') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')



    def press_four_btn6_9_7_1(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.winner.append('2')
            
    def press_four_btn6_9_7_4(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.btn_9.setText('X')
            self.winner.append('9')

    def press_four_btn6_9_7_2(self):
        if self.list.count('6') == 1 and self.list.count('9') == 1 and self.list.count('7') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')



    def press_four_btn7_1_6_9(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.btn_3.setText('  ')
            self.winner.append('2')
            
    def press_four_btn7_1_6_3(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_2.setText('O')
            self.btn_9.setText('  ')
            self.winner.append('2')


    def press_four_btn7_1_6_2(self):
        if self.list.count('7') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn7_8_1_2(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')
            
    def press_four_btn7_8_1_3(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_6.setText('O')
            self.winner.append('6')


    def press_four_btn7_8_1_6(self):
        if self.list.count('7') == 1 and self.list.count('8') == 1 and self.list.count('1') == 1 and self.list.count('6') == 1 and  len(self.list) == 4:
            self.btn_3.setText('O')
            self.winner.append('3')



    def press_four_btn7_9_2_1(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')
            
    def press_four_btn7_9_2_3(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')


    def press_four_btn7_9_2_4(self):
        if self.list.count('7') == 1 and self.list.count('9') == 1 and self.list.count('2') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')


    def press_four_btn8_2_3_9(self):
        if self.list.count('8') == 1 and self.list.count('2') == 1 and self.list.count('3') == 1 and self.list.count('9') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.btn_6.setText('  ')
            self.winner.append('4')



    def press_four_btn8_9_3_1(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('1') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn8_9_3_2(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('2') == 1 and  len(self.list) == 4:
            self.btn_4.setText('O')
            self.winner.append('4')

    def press_four_btn8_9_3_4(self):
        if self.list.count('8') == 1 and self.list.count('9') == 1 and self.list.count('3') == 1 and self.list.count('4') == 1 and  len(self.list) == 4:
            self.btn_1.setText('O')
            self.winner.append('1')


    def press_btn_try_agin(self):
        self.list = list()
        self.btn_1.setText('')
        self.btn_2.setText('')
        self.btn_3.setText('')
        self.btn_4.setText('')
        self.btn_5.setText('')
        self.btn_6.setText('')
        self.btn_7.setText('')
        self.btn_8.setText('')
        self.btn_9.setText('')
    


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())




