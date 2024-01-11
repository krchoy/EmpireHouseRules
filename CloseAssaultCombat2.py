"""Close Assault Combat Assistant using Tkinter"""

import tkinter as tk

class CAC_Window(tk.Tk):
    """Root window """

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
        # set the title
        self.title('Close Assault Combat Assistant')

        # set the root window size
        self.geometry('640x480+300+300')
        self.resizable(True, True)

    


###############
# Execute App #
###############

root = CAC_Window()
root.mainloop() 

