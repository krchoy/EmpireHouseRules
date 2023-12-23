from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QComboBox, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
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
 
        attackerUI = QVBoxLayout()
        label_1 = QLabel("Attacker Morale Grade")
        label_1.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.moraleGradeAttacker = QComboBox(self)
        self.moraleGradeAttacker.addItems(self.MoraleGrades)
        attackerUI.addWidget(label_1)
        attackerUI.addWidget(self.moraleGradeAttacker)

        
        defenderUI = QVBoxLayout()
        label_2 = QLabel("Defender Morale Grade")
        label_2.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.moraleGradeDefender = QComboBox(self)
        self.moraleGradeDefender.addItems(self.MoraleGrades)
        defenderUI.addWidget(label_2)
        defenderUI.addWidget(self.moraleGradeDefender)

        setMoraleUI = QVBoxLayout()
        moraleSelectedBN = QPushButton("Morale Selected", self)
        moraleSelectedBN.clicked.connect(self.MoraleSelected)
        setMoraleUI.addWidget(moraleSelectedBN)

        self.label_3 = QLabel("inert")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.upperPaneUI = QGridLayout()        
        self.upperPaneUI.addLayout(attackerUI, 0, 0)
        self.upperPaneUI.addLayout(setMoraleUI, 0, 1)
        self.upperPaneUI.addLayout(defenderUI, 0, 2)
        self.upperPaneUI.addWidget(self.label_3, 1, 1)
        self.setLayout(self.upperPaneUI)
        self.setGeometry(500, 500, 200, 200)
        self.setWindowTitle('Close Assault Combat')
        self.show()

    def MoraleSelected(self):

#        self.moraleGradeAttacker.hide()
#        self.moraleGradeDefender.disable()
        
        print(self.moraleGradeAttacker.currentText())
        print(self.moraleGradeAttacker.currentIndex())        
        print(self.MoraleGrades_Initial_Row[self.moraleGradeAttacker.currentText()])
        self.label_3.setText(self.moraleGradeAttacker.currentText() + str(self.moraleGradeAttacker.currentIndex()))
        self.moraleGradeAttackerRowStart = self.MoraleGrades_Initial_Row[self.moraleGradeAttacker.currentIndex()]
        print(self.moraleGradeAttackerRowStart)
        print(self.CloseAssaultCombatTable[self.moraleGradeAttackerRowStart])
        


app = QApplication(sys.argv)
window = CAC_Window()
window.show()
sys.exit(app.exec())
