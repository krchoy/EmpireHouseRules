from PyQt6.QtWidgets import QGroupBox, QButtonGroup, QApplication, QSlider, QWidget, QLabel, QComboBox, QHBoxLayout,QVBoxLayout, QGridLayout, QPushButton, QRadioButton
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

        self.grid = QGridLayout()

        self.CAC_Row1()
        self.CAC_Row2()
        self.CAC_Row3()
        self.CAC_Row4()
        self.CAC_Row5()
##        self.CAC_Row6()
        self.CAC_Row7()
        
        self.setLayout(self.grid)
        self.show()

    def CAC_Row1(self):
        label1 = QLabel("Every 2 figures lost since start of day")
        slider1 = QSlider(Qt.Orientation.Horizontal, self)
        slider1.setGeometry(50,50, 200, 50)
        slider1.setMinimum(0)
        slider1.setMaximum(12)
        slider1.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider1.setTickInterval(1)
        slider1.valueChanged.connect(self.displaySlider1) 
        self.result1 = QLabel("")
        self.grid.addWidget(label1, 0, 0)
        self.grid.addWidget(slider1, 0, 1)
        self.grid.addWidget(self.result1, 0, 2)

    def CAC_Row2(self):
        label2= QLabel("Every Fatigue Point accumulated")
        slider2 = QSlider(Qt.Orientation.Horizontal, self)
        slider2.setGeometry(50,50, 200, 50)
        slider2.setMinimum(0)
        slider2.setMaximum(12)
        slider2.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider2.setTickInterval(1)
        slider2.valueChanged.connect(self.displaySlider2) 
        self.result2 = QLabel("")
        self.grid.addWidget(label2, 1, 0)
        self.grid.addWidget(slider2, 1, 1)
        self.grid.addWidget(self.result2, 1, 2)
        
    def CAC_Row3(self):
        label3 = QLabel("Unit is:")
        vbox3 = QVBoxLayout()
        label3.setStyleSheet("""color: "black"; background-color: "green";""")
        TitlesR3 = [
            'Good',
            'Disordered',
            'Blown',
            'Blown & Disordered',
            'Broken' ]
        ButtonsR3 = [QRadioButton(title) for title in TitlesR3]
        
        ButtonGroupR3 = QButtonGroup(self)
        for ButtonR3 in ButtonsR3:
            vbox3.addWidget(ButtonR3)
            ButtonR3.toggled.connect(self.showRadio3Result)
            ButtonGroupR3.addButton(ButtonR3)
            ButtonR3.setStyleSheet("""color: "black"; background-color: "green";""")
        
        self.result3 = QLabel("")

        self.grid.addWidget(label3, 2, 0)
        self.grid.addLayout(vbox3, 2, 1)
        self.grid.addWidget(self.result3, 2, 2)

    def CAC_Row4(self):
        label4 = QLabel("Attached Leadership at:")
        vbox4 = QVBoxLayout()
        TitlesR4 = [
            "None",
            "Charismatic Div or Brig",
            "Charismatic Reg or below",
            "Inspiring Div or Brig",
            "Inspiring Reg or below",
            "Fine Unit leader attached to sub unit",
            "Contemptible Div or Brig",
            "Contemptible Reg or below"
            ]
        ButtonsR4 = [QRadioButton(title) for title in TitlesR4]
        ButtonGroupR4 = QButtonGroup(self)
        
        for ButtonR4 in ButtonsR4:
            vbox4.addWidget(ButtonR4)
            ButtonR4.toggled.connect(self.showRadio4Result)
            ButtonGroupR4.addButton(ButtonR4)

        self.result4 = QLabel("")

        self.grid.addWidget(label4, 3, 0)
        self.grid.addLayout(vbox4, 3, 1)
        self.grid.addWidget(self.result4, 3, 2)

    def CAC_Row5(self):

        label5 = QLabel("Unit is attacking:")
        label5.setStyleSheet("""color: "black"; background-color: "green";""")
        vbox5 = QVBoxLayout()
        TitlesR5 = [
            "Front",
            "Flank",
            "Rear",
            "with Partial Enfilade",
            "with Full Enfilade"
            ]
        ButtonsR5 = [QRadioButton(title) for title in TitlesR5]
        ButtonGroupR5 = QButtonGroup(self)
        
        for ButtonR5 in ButtonsR5:
            vbox5.addWidget(ButtonR5)
            ButtonR5.toggled.connect(self.showRadio5Result)
            ButtonGroupR5.addButton(ButtonR5)
            ButtonR5.setStyleSheet("""color: "black"; background-color: "green";""")
                
        self.result5 = QLabel("")

        self.grid.addWidget(label5, 4, 0)
        self.grid.addLayout(vbox5, 4, 1)
        self.grid.addWidget(self.result5, 4, 2)
    def CAC_Row6(self):
        label6 = QLabel("Unit atacking into cover that is:")
        vbox6 = QVBoxLayout()
        TitlesR6 = [
            "None",
            "Light",
            "Medium",
            "Heavy",
            "Extra Heavy",
            "Super Heavy",
            ]
        ButtonsR6 = [QRadioButton(title) for title in TitlesR6]
        ButtonGroupR6 = QButtonGroup(self)
        
        for ButtonR6 in ButtonsR6:
            vbox6.addWidget(ButtonR6)
            ButtonR6.toggled.connect(self.showRadio6Result)
            ButtonGroupR6.addButton(ButtonR6)

        self.result6 = QLabel("")

        self.grid.addWidget(label6, 5, 0)
        self.grid.addLayout(vbox6, 5, 1)
        self.grid.addWidget(self.result6, 5, 2)

    def CAC_Row7(self):
        label7 = QLabel("Formed:")
        vbox7 = QVBoxLayout()
        TitlesR7 = [
            "... versus Unformed(incl. Gunners)",
            "... Infantry not square or Closed Column versus Closed Column",
            "... Infantry not square or Closed Column versus Square",
            ]
        ButtonsR7 = [QRadioButton(title) for title in TitlesR7]
        ButtonGroupR7 = QButtonGroup(self)
        
        for ButtonR7 in ButtonsR7:
            vbox7.addWidget(ButtonR7)
            ButtonR7.toggled.connect(self.showRadio7Result)
            ButtonGroupR7.addButton(ButtonR7)

        self.result7 = QLabel("")

        self.grid.addWidget(label7, 6, 0)
        self.grid.addLayout(vbox7, 6, 1)
        self.grid.addWidget(self.result7, 6, 2)
        
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
    def showRadio5Result(self):
        self.result5.setText(str(self.sender().text()))
    def showRadio6Result(self):
        self.result6.setText(str(self.sender().text()))
    def showRadio7Result(self):
        self.result7.setText(str(self.sender().text()))

app = QApplication(sys.argv)
window = CAC_Modifiers_UI()

app.setStyleSheet("""
    QWidget {
        background-color: "green";
        color: "white";
    }
    QRadioButton {
        
        background-color: "green"
    }
    QLineEdit {
        background-color: "white";
        color: "black";
    }
""")
window.show()
sys.exit(app.exec())
