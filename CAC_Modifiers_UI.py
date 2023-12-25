from PyQt6.QtWidgets import QApplication, QSlider, QWidget, QLabel, QComboBox, QHBoxLayout,QVBoxLayout, QGridLayout, QPushButton, QRadioButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class CAC_Modifiers_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.CAC_UI()

    def CAC_UI(self):
        self.setWindowTitle("Close Assault Combat Modifiers")
        self.setWindowIcon(QIcon("icon.jpg"))

        grid = QGridLayout()

        label1 = QLabel("Every 2 figures lost since start of day")
        slider1 = QSlider(Qt.Orientation.Horizontal, self)
        slider1.setGeometry(50,50, 200, 50)
        slider1.setMinimum(0)
        slider1.setMaximum(12)
        slider1.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider1.setTickInterval(1)
        slider1.valueChanged.connect(self.displaySlider1) 
        self.result1 = QLabel("")
        grid.addWidget(label1, 0, 0)
        grid.addWidget(slider1, 0, 1)
        grid.addWidget(self.result1, 0, 2)
        
        
        label2= QLabel("Every Fatigue Point accumulated")
        slider2 = QSlider(Qt.Orientation.Horizontal, self)
        slider2.setGeometry(50,50, 200, 50)
        slider2.setMinimum(0)
        slider2.setMaximum(12)
        slider2.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider2.setTickInterval(1)
        slider2.valueChanged.connect(self.displaySlider2) 
        self.result2 = QLabel("")
        grid.addWidget(label2, 1, 0)
        grid.addWidget(slider2, 1, 1)
        grid.addWidget(self.result2, 1, 2)

        label3 = QLabel("Unit is:")
        self.radio30 = QRadioButton("Good", self)
        self.radio31 = QRadioButton("Disordered", self)
        self.radio32 = QRadioButton("Blown", self)
        self.radio33 = QRadioButton("Blown & Disordered", self)
        self.radio34 = QRadioButton("Broken", self)
        self.radio30.toggled.connect(self.showRadio3Result)
        self.radio31.toggled.connect(self.showRadio3Result)
        self.radio32.toggled.connect(self.showRadio3Result)
        self.radio33.toggled.connect(self.showRadio3Result)
        self.radio34.toggled.connect(self.showRadio3Result)
        self.result3 = QLabel("")
        
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.radio30)
        vbox3.addWidget(self.radio31)
        vbox3.addWidget(self.radio32)
        vbox3.addWidget(self.radio33)
        vbox3.addWidget(self.radio34)

        grid.addWidget(label3, 2, 0)
        grid.addLayout(vbox3, 2, 1)
        grid.addWidget(self.result3, 2, 2)

        label4 = QLabel("Attached Ledership at:")
        self.radio40 = QRadioButton("None", self)
        self.radio41 = QRadioButton("Charismatic Div or Brig", self)
        self.radio42 = QRadioButton("Charismatic Reg or below", self)
        self.radio43 = QRadioButton("Inspiring Div or Brig", self)
        self.radio44 = QRadioButton("Inspiring Reg or below", self)
        self.radio45 = QRadioButton("Fine Unit leader attached to sub unit", self)
        self.radio46 = QRadioButton("Contemptible Div or Brig", self)
        self.radio47 = QRadioButton("Contemptible Reg or below", self)
        self.radio40.toggled.connect(self.showRadio4Result)
        self.radio41.toggled.connect(self.showRadio4Result)
        self.radio42.toggled.connect(self.showRadio4Result)
        self.radio43.toggled.connect(self.showRadio4Result)
        self.radio44.toggled.connect(self.showRadio4Result)
        self.radio45.toggled.connect(self.showRadio4Result)
        self.radio46.toggled.connect(self.showRadio4Result)
        self.radio47.toggled.connect(self.showRadio4Result)
 
        self.result4 = QLabel("")
        
        vbox4 = QVBoxLayout()
        vbox4.addWidget(self.radio40)
        vbox4.addWidget(self.radio41)
        vbox4.addWidget(self.radio42)
        vbox4.addWidget(self.radio43)
        vbox4.addWidget(self.radio44)
        vbox4.addWidget(self.radio45)
        vbox4.addWidget(self.radio46)
        vbox4.addWidget(self.radio47)
        grid.addWidget(label4, 3, 0)
        grid.addLayout(vbox4, 3, 1)
        grid.addWidget(self.result4, 3, 2)

        
        self.setLayout(grid)
        self.show()

        
    def displaySlider1(self, result):
        self.result1.setText(str(self.sender().value()))
        self.result1.adjustSize()
    def displaySlider2(self, result):
        self.result2.setText(str(self.sender().value()))
        self.result2.adjustSize()
    def showRadio3Result(self):
        self.result3.setText(str(self.sender().text()))
    def showRadio4Result(self):
        self.result4.setText(str(self.sender().text()))

app = QApplication(sys.argv)
window = CAC_Modifiers_UI()
window.show()
sys.exit(app.exec())
