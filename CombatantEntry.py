from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QComboBox, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

class CombatantEntry(QVBoxLayout):
    def __init__(self, master, label, cellModifier=0):
        super().__init__(master)

        MoraleGrades_Initial_Row = {'VOL': 10, 'TM': 14, 'LW': 17, 'CON': 18,
                                   'VET': 20, 'CRK': 22, 'ELT': 23, 'GRN': 24, 'GRD': 25, 'OG': 27}
        MoraleGrades = ['', ]
        for name in MoraleGrades_Initial_Row.keys():
            MoraleGrades.append(name)
            
        self.CloseAssaultCombatTable = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3,
                           3, 4, 4, 5, 5, 6, 6, 7, 8, 9,
                           10, 11, 12, 14, 16, 18, 20, 22, 24, 27,
                           30, 35, 40, 45, 50, 55, 62, 40, 80, 90,
                           100, 110, 120, 140, 160, 180, 200, 220, 240, 270,
                           300, 350, 400, 450, 500, 550, 620, 700, 800, 900]

        label_1 = QLabel(label)
        label_1.setAlignment(Qt.AlignmentFlag.AlignTop)
        moraleGrade = QComboBox(master)
        moraleGrade.addItems(MoraleGrades)
        self.addWidget(label_1)
        self.addWidget(moraleGrade)
        print(label)

##        cellModifier=MoraleGrades_Initial_Row[moraleGrade.currentText()]
##        print(str(cellModifier)+label)
