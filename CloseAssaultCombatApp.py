from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QComboBox, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
 
class Window(QWidget):

    
    def __init__(self):
        super().__init__()

        MoraleGrades_Initial_Row = {'VOL': 10, 'TM': 14, 'LW': 17, 'CON': 18,
                                   'VET': 20, 'CRK': 22, 'ELT': 23, 'GRN': 24, 'GRD': 25, 'OG': 27}
        self.MoraleGrades = ['', ]
        for name in MoraleGrades_Initial_Row.keys():
            self.MoraleGrades.append(name)

        self.UI()
    

    def UI(self):    
        
        self.setWindowTitle("Close Assault Combat")
        self.setWindowIcon(QIcon("icon.jpg"))
 
        attackerUI = QVBoxLayout()
        label_1 = QLabel("Attacker Morale Grade")
        label_1.setAlignment(Qt.AlignmentFlag.AlignTop)
        moraleGradeAttacker = QComboBox(self)
        moraleGradeAttacker.addItems(self.MoraleGrades)
        attackerUI.addWidget(label_1)
        attackerUI.addWidget(moraleGradeAttacker)

        
        defenderUI = QVBoxLayout()
        label_2 = QLabel("Defender Morale Grade")
        label_2.setAlignment(Qt.AlignmentFlag.AlignTop)
        moraleGradeDefender = QComboBox(self)
        moraleGradeDefender.addItems(self.MoraleGrades)
        defenderUI.addWidget(label_2)
        defenderUI.addWidget(moraleGradeDefender)

        setMoraleUI = QVBoxLayout()
        moraleSelectedBN = QPushButton("Morale Selected", self)
        setMoraleUI.addWidget(moraleSelectedBN)

        upperPaneUI = QGridLayout()        
        upperPaneUI.addLayout(attackerUI, 0, 0)
        upperPaneUI.addLayout(setMoraleUI, 0, 1)
        upperPaneUI.addLayout(defenderUI, 0, 2)
        self.setLayout(upperPaneUI)
        self.setGeometry(500, 500, 200, 200)
        self.setWindowTitle('Close Assault Combat')
        self.show()
        

 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
