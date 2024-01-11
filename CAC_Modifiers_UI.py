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
        self.CAC_Row9()
        self.CAC_Row10()
        self.CAC_Row11()
        self.CAC_Row12()
        self.CAC_Row13()
        self.CAC_Row14()
        self.CAC_Row15()
        
        self.setLayout(self.grid)
##        self.show()

    def CAC_Row1(self):
        label1 = QLabel("Every 2 figures lost since start of day")
        label1.setStyleSheet("""color: "black"; background-color: "grey";""")
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
        label2.setStyleSheet("""color: "black"; background-color: "lightgrey";""")
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
        label3.setStyleSheet("""color: "black"; background-color: "grey";""")
        vbox3 = QVBoxLayout()
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
        label4.setStyleSheet("""color: "black"; background-color: "lightgrey";""")
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
        label5.setStyleSheet("""color: "black"; background-color: "grey";""")
        vbox5 = QVBoxLayout()
        TitlesR5 = [
            "with no advantage",
            "the Flank",
            "the Rear",
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
        label6.setStyleSheet("""color: "black"; background-color: "lightgrey";""")
        vbox6 = QVBoxLayout()
        TitlesR6 = [
            "with no advantages",
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
        label7 = QLabel("Cavalry attacking Infantry:")
        label7.setStyleSheet("""color: "black"; background-color: "lightpink";""")
        vbox7 = QVBoxLayout()
        TitlesR7 = [
            "with no advantages",
            "Cavalry versus Infantry Closed Column",
            "Cavalry versus Infantry Square",
            "Veteran or higher grade Lancers versus Infantry Closed Column",
            "Veteran or higher grade Lancers versus Infantry Square",
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
        label8 = QLabel("Cavalry versus Cavalry:")
        label8.setStyleSheet("""color: "black"; background-color: "mistyrose";""")
        vbox8 = QVBoxLayout()
        TitlesR8 = [
            "with no advantages",
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


    def CAC_Row9(self):
        label9 = QLabel("Cavalry attacking Cavalry:")
        label9.setStyleSheet("""color: "black"; background-color: "lightpink";""")
        vbox9 = QVBoxLayout()
        TitlesR9 = [
            "with no advantages",
            "Veteran or higher grade Lancers Charging Lancers",
            ]
        ComboBoxR9 = QComboBox(self)
        ComboBoxR9.addItems(TitlesR9)
        ComboBoxR9.currentIndexChanged.connect(self.selectionChange9)
        vbox9.addWidget(ComboBoxR9)

        self.result9 = QLabel("")

        self.grid.addWidget(label9, 8, 0)
        self.grid.addLayout(vbox9, 8, 1)
        self.grid.addWidget(self.result9, 8, 2)

    def CAC_Row10(self):
        label10 = QLabel("Cavalry charging:")
        label10.setStyleSheet("""color: "black"; background-color: "mistyrose";""")
        vbox10 = QVBoxLayout()
        TitlesR10 = [
            "with no advantages",
            "Non-Charging Cavalry",
            ]
        ComboBoxR10 = QComboBox(self)
        ComboBoxR10.addItems(TitlesR10)
        ComboBoxR10.currentIndexChanged.connect(self.selectionChange10)
        vbox10.addWidget(ComboBoxR10)

        self.result10 = QLabel("")

        self.grid.addWidget(label10, 9, 0)
        self.grid.addLayout(vbox10, 9, 1)
        self.grid.addWidget(self.result10, 9, 2)

    def CAC_Row11(self):
        label11 = QLabel("Formed Infantry:")
        label11.setStyleSheet("""color: "black"; background-color: "lightblue";""")
        vbox11 = QVBoxLayout()
        TitlesR11 = [
            "with no advantages",
            "... Infantry not square or Closed Column versus Closed Column",
            "... Infantry not square or Closed Column versus Square",
            ]
        ComboBoxR11 = QComboBox(self)
        ComboBoxR11.addItems(TitlesR11)
        ComboBoxR11.currentIndexChanged.connect(self.selectionChange11)
        vbox11.addWidget(ComboBoxR11)

        self.result11 = QLabel("")

        self.grid.addWidget(label11, 10, 0)
        self.grid.addLayout(vbox11, 10, 1)
        self.grid.addWidget(self.result11, 10, 2)

    def CAC_Row12(self):
        label12 = QLabel("Infantry:")
        label12.setStyleSheet("""color: "black"; background-color: "steelgrey";""")
        vbox12 = QVBoxLayout()
        TitlesR12 = [
            "with no advantages",
            "... in Closed Column versus Cavalry",
            "... in Hasty Square versus Cavalry",
            "... in Ordered Square versus Cavalry",
            ]
        ComboBoxR12 = QComboBox(self)
        ComboBoxR12.addItems(TitlesR12)
        ComboBoxR12.currentIndexChanged.connect(self.selectionChange12)
        vbox12.addWidget(ComboBoxR12)

        self.result12 = QLabel("")

        self.grid.addWidget(label12, 11, 0)
        self.grid.addLayout(vbox12, 11, 1)
        self.grid.addWidget(self.result12, 11, 2)

    def CAC_Row13(self):
        label13 = QLabel("Infantry Numerical Advantage :")
        vbox13 = QVBoxLayout()
        TitlesR13 = [
            "with no advantages",
            "versus Infantry or Gunners 2:1",
            "versus Infantry or Gunners 3:1",
            "versus Infantry or Gunners 4:1",
            ]
        ComboBoxR13 = QComboBox(self)
        ComboBoxR13.addItems(TitlesR13)
        ComboBoxR13.currentIndexChanged.connect(self.selectionChange13)
        vbox13.addWidget(ComboBoxR13)

        self.result13 = QLabel("")

        self.grid.addWidget(label13, 12, 0)
        self.grid.addLayout(vbox13, 12, 1)
        self.grid.addWidget(self.result13, 12, 2)
        
    def CAC_Row14(self):
        label14 = QLabel("Unit atacking into cover that is:")
        vbox14 = QVBoxLayout()
        TitlesR14 = [
            "None",
            "Light",
            "Medium",
            "Heavy",
            "Extra Heavy",
            "Super Heavy",
            ]
        ComboBoxR14 = QComboBox(self)
        ComboBoxR14.addItems(TitlesR14)
        ComboBoxR14.currentIndexChanged.connect(self.selectionChange14)
        vbox14.addWidget(ComboBoxR14)

        self.result14 = QLabel("")

        self.grid.addWidget(label14, 13, 0)
        self.grid.addLayout(vbox14, 13, 1)
        self.grid.addWidget(self.result14, 13, 2)

    def CAC_Row15(self):
        label15 = QLabel("Engineers attached attacking structure")
        vbox15 = QVBoxLayout()
        TitlesR15 = [
            "None",
            "Engineers attached to a unit attacking a structure",
            "French Guard Engineers attached to a unit attacking a structure",
            ]
        ComboBoxR15 = QComboBox(self)
        ComboBoxR15.addItems(TitlesR15)
        ComboBoxR15.currentIndexChanged.connect(self.selectionChange15)
        vbox15.addWidget(ComboBoxR15)

        self.result15 = QLabel("")

        self.grid.addWidget(label15, 14, 0)
        self.grid.addLayout(vbox15, 14, 1)
        self.grid.addWidget(self.result15, 14, 2)
        
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
    def selectionChange9(self):
        self.result9.setText(str(self.sender().currentText()))
    def selectionChange10(self):
        self.result10.setText(str(self.sender().currentText()))
    def selectionChange11(self):
        self.result11.setText(str(self.sender().currentText()))
    def selectionChange12(self):
        self.result12.setText(str(self.sender().currentText()))
    def selectionChange13(self):
        self.result13.setText(str(self.sender().currentText()))
    def selectionChange14(self):
        self.result14.setText(str(self.sender().currentText()))
    def selectionChange15(self):
        self.result15.setText(str(self.sender().currentText()))


##app = QApplication(sys.argv)
##window = CAC_Modifiers_UI()

##app.setStyleSheet("""
##    QWidget {
##        background-color: "seashell";
##        color: "black";
##    }
##    QComboBox {
##        
##        background-color: "seashell"
##    }
##    QLineEdit {
##        background-color: "white";
##        color: "black";
##    }
##""")
##window.show()
##sys.exit(app.exec())
