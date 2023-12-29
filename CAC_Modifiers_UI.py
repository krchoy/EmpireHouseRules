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
        self.CAC_Row6()
        self.CAC_Row7()
        self.CAC_Row8()
        self.CAC_Row13()

        
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
        label3 = QLabel("Unit morale is:")
        vbox3 = QVBoxLayout()
        label3.setStyleSheet("""color: "black"; background-color: "green";""")
        TitlesR3 = [
            'Good',
            'Disordered',
            'Blown',
            'Blown & Disordered',
            'Broken' ]
        ComboBoxR3 = QComboBox(self)
        ComboBoxR3.addItems(TitlesR3)
        ComboBoxR3.currentIndexChanged.connect(self.selectionChange3)
        vbox3.addWidget(ComboBoxR3)
        
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
        ComboBoxR4 = QComboBox(self)
        ComboBoxR4.addItems(TitlesR4)
        ComboBoxR4.currentIndexChanged.connect(self.selectionChange4)
        vbox4.addWidget(ComboBoxR4)

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
        ComboBoxR5 = QComboBox(self)
        ComboBoxR5.addItems(TitlesR5)
        ComboBoxR5.currentIndexChanged.connect(self.selectionChange5)
        vbox5.addWidget(ComboBoxR5)
                
        self.result5 = QLabel("")

        self.grid.addWidget(label5, 4, 0)
        self.grid.addLayout(vbox5, 4, 1)
        self.grid.addWidget(self.result5, 4, 2)
        
    def CAC_Row6(self):
        label6 = QLabel("Formed:")
        vbox6 = QVBoxLayout()
        TitlesR6 = [
            "Not applicable",
            "... versus Unformed(incl. Gunners)",
            ]
        ComboBoxR6 = QComboBox(self)
        ComboBoxR6.addItems(TitlesR6)
        ComboBoxR6.currentIndexChanged.connect(self.selectionChange6)
        vbox6.addWidget(ComboBoxR6)


        self.result6 = QLabel("")

        self.grid.addWidget(label6, 5, 0)
        self.grid.addLayout(vbox6, 5, 1)
        self.grid.addWidget(self.result6, 5, 2)

    def CAC_Row7(self):
        label7 = QLabel("Formed Infantry:")
        vbox7 = QVBoxLayout()
        TitlesR7 = [
            "Not applicable",
            "... Infantry not square or Closed Column versus Closed Column",
            "... Infantry not square or Closed Column versus Square",
            ]
        ComboBoxR7 = QComboBox(self)
        ComboBoxR7.addItems(TitlesR7)
        ComboBoxR7.currentIndexChanged.connect(self.selectionChange7)
        vbox7.addWidget(ComboBoxR7)


        self.result7 = QLabel("")

        self.grid.addWidget(label7, 6, 0)
        self.grid.addLayout(vbox7, 6, 1)
        self.grid.addWidget(self.result7, 6, 2)


    def CAC_Row8(self):
        label8 = QLabel("Cavalry attacking:")
        vbox8 = QVBoxLayout()
        TitlesR8 = [
            "Not applicable",
            "Cavalry versus Infantry Closed Column",
            "Cavalry versus Infantry Square",
            "Veteran or higher grade Lancers versus Infantry Closed Column",
            "Veteran or higher grade Lancers versus Infantry Square",
            "Shock Cavalry versus Regular Cavalry",
            "Shock Cavalry versus Irregular Cavalry",
            "Regular Cavalry versus Irregular Cavalry",
            ]
        ComboBoxR8 = QComboBox(self)
        ComboBoxR8.addItems(TitlesR8)
        ComboBoxR8.currentIndexChanged.connect(self.selectionChange8)
        vbox8.addWidget(ComboBoxR8)


        self.result8 = QLabel("")

        self.grid.addWidget(label8, 7, 0)
        self.grid.addLayout(vbox8, 7, 1)
        self.grid.addWidget(self.result8, 7, 2)

    def CAC_Row13(self):
        label13 = QLabel("Unit atacking into cover that is:")
        vbox13 = QVBoxLayout()
        TitlesR13 = [
            "None",
            "Light",
            "Medium",
            "Heavy",
            "Extra Heavy",
            "Super Heavy",
            ]
        ComboBoxR13 = QComboBox(self)
        ComboBoxR13.addItems(TitlesR13)
        ComboBoxR13.currentIndexChanged.connect(self.selectionChange13)
        vbox13.addWidget(ComboBoxR13)

        self.result13 = QLabel("")

        self.grid.addWidget(label13, 12, 0)
        self.grid.addLayout(vbox13, 12, 1)
        self.grid.addWidget(self.result13, 12, 2)

        
        
    def displaySlider1(self, result):
        self.result1.setText(str(self.sender().value()))
        self.result1.adjustSize()
    def displaySlider2(self, result):
        self.result2.setText(str(self.sender().value()))
        self.result2.adjustSize()
    def selectionChange3(self):
        self.result3.setText(str(self.sender().currentText()))
    def selectionChange4(self):
        self.result4.setText(str(self.sender().currentText()))
    def selectionChange5(self):
        self.result5.setText(str(self.sender().currentText()))
    def selectionChange6(self):
        self.result6.setText(str(self.sender().currentText()))
    def selectionChange7(self):
        self.result7.setText(str(self.sender().currentText()))
    def selectionChange8(self):
        self.result8.setText(str(self.sender().currentText()))
    def selectionChange13(self):
        self.result13.setText(str(self.sender().currentText()))


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
