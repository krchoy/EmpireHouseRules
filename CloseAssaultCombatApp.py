from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QComboBox, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from CombatantEntry import *

import sys
 
class CAC_Window(QWidget):

    
    def __init__(self):
        super().__init__()

        self.MoraleGrades_Initial_Row = {'VOL': 10, 'TM': 14, 'LW': 17, 'CON': 18,
                                   'VET': 20, 'CRK': 22, 'ELT': 23, 'GRN': 24, 'GRD': 25, 'OG': 27}
        self.MoraleGrades = ['', ]
        for name in self.MoraleGrades_Initial_Row.keys():
            self.MoraleGrades.append(name)
            
        self.CloseAssaultCombatTable = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3,
                           3, 4, 4, 5, 5, 6, 6, 7, 8, 9,
                           10, 11, 12, 14, 16, 18, 20, 22, 24, 27,
                           30, 35, 40, 45, 50, 55, 62, 40, 80, 90,
                           100, 110, 120, 140, 160, 180, 200, 220, 240, 270,
                           300, 350, 400, 450, 500, 550, 620, 700, 800, 900]    

        self.UI()
    

    def UI(self):    
        
        self.setWindowTitle("Close Assault Combat")
        self.setWindowIcon(QIcon("icon.jpg"))
        AttackModifier=0
        attacker = CombatantEntry(self, "Attacker", AttackModifier)
        print(attacker)
        DefendModifier=0
        defender = CombatantEntry(self, "Defender", DefendModifier)
        print(defender)
        

        
##        defenderUI = QVBoxLayout()
##        label_2 = QLabel("Defender Morale Grade")
##        label_2.setAlignment(Qt.AlignmentFlag.AlignTop)
##        self.moraleGradeDefender = QComboBox(self)
##        self.moraleGradeDefender.addItems(self.MoraleGrades)
##        defenderUI.addWidget(label_2)
##        defenderUI.addWidget(self.moraleGradeDefender)
##
        setMoraleUI = QVBoxLayout()
        moraleSelectedBN = QPushButton("Morale Selected", self)
        moraleSelectedBN.clicked.connect(self.MoraleSelected)
        setMoraleUI.addWidget(moraleSelectedBN)
        
        self.label_3 = QLabel("inert")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom)


##        Attacker_Modifiers = self.CAC_UI("Attacker")
##
##        Defender_Modifiers = self.CAC_UI("Defender")
##        

        self.upperPaneUI = QGridLayout()        
        self.upperPaneUI.addLayout(attacker, 0, 0)
        self.upperPaneUI.addLayout(setMoraleUI, 0, 1)
        self.upperPaneUI.addLayout(defender, 0, 2)
##        self.upperPaneUI.addWidget(Attacker_Modifiers, 1, 0)
##        self.upperPaneUI.addWidget(Defender_Modifiers, 1, 2)
        self.upperPaneUI.addWidget(self.label_3, 2, 1)
        self.setLayout(self.upperPaneUI)
        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle('Close Assault Combat')
        self.show()

        
        
    def MoraleSelected(self):
##        print(self.moraleGradeAttacker.currentText())
##        print(self.moraleGradeAttacker.currentIndex())        
##        print(self.MoraleGrades_Initial_Row[self.moraleGradeAttacker.currentText()])
        
        
        self.moraleGradeAttackerRowStart = self.MoraleGrades_Initial_Row[self.moraleGradeAttacker.currentText()]
        print(self.moraleGradeAttackerRowStart)
        print(self.CloseAssaultCombatTable[self.moraleGradeAttackerRowStart])
        
        self.moraleGradeDefenderRowStart = self.MoraleGrades_Initial_Row[self.moraleGradeDefender.currentText()]

        
        self.label_3.setText(str(self.CloseAssaultCombatTable[self.moraleGradeAttackerRowStart]) + " " + str(self.CloseAssaultCombatTable[self.moraleGradeDefenderRowStart]))

    def CAC_UI(self, combatant):
       print(combatant)
##        self.setWindowTitle("Close Assault Combat Modifiers")
##        self.setWindowIcon(QIcon("icon.jpg"))

##        self.grid = QGridLayout()
##
##        self.CAC_Row1()
##        self.CAC_Row2()
##        self.CAC_Row3()
##        self.CAC_Row4()
##        self.CAC_Row5()
##        self.CAC_Row6()
##        self.CAC_Row7()
##        self.CAC_Row8()
##        self.CAC_Row9()
##        self.CAC_Row10()
##        self.CAC_Row11()
##        self.CAC_Row12()
##        self.CAC_Row13()
##        self.CAC_Row14()
##        self.CAC_Row15()
        
##        self.setLayout(self.grid)
##        self.show()
        

app = QApplication(sys.argv)
window = CAC_Window()
window.show()
sys.exit(app.exec())
