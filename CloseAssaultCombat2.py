"""Close Assault Combat Assistant using Tkinter"""

import tkinter as tk
from tkinter import ttk

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
        #use a common frame to input attacker and defender modifiers
        AttackModifier=0
        attacker = CombatantEntry(self, "Attacker", AttackModifier)
        attacker.grid(row=1, column=0)

        label = tk.Label(
            self,
            text="space",
            )
        label.grid(row=2, column=1)        
        DefendModifier=0
        defender = CombatantEntry(self, "Defender", DefendModifier)
        defender.grid(row=1, column=2)
        
    


class CombatantEntry(tk.Frame):
    """Frame reused for attaker and defender attributes entry """
    def __init__(self, parent, combatant, cellModifier):
        super().__init__(parent)

        
        self.label = tk.Label(
            self,
            text=combatant,
            anchor='w',
            font=('TkHeadingFont 16 bold')
            )

        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.label = tk.Label(
            self,
            text='Modifiers',
            anchor='w',
            font=('TkDefaultFont 10 normal')
            )

        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        ##
        label1 = tk.Label(
            self,
            text="Every 2 figures lost since start of day")
        result1 = tk.Spinbox(
            self,
            from_=0,
            to=12,
            increment=1)
        label1.grid()
        result1.grid()
        ##
        label2 = tk.Label(
            self,
            text="Every Fatigue Point accumulated")
        result2 = tk.Spinbox(
            self,
            from_=0,
            to=12,
            increment=1)
        label2.grid()
        result2.grid()
        ##
        label3 = tk.Label(
            self,
            text="Unit morale is:")
        tr3 = tk.StringVar()
        result3 = ttk.Combobox(
            self,
            height=1,
            textvariable=tr3
            )
        result3['values'] = (
            'Good',
            'Disordered',
            'Blown',
            'Blown & Disordered',
            'Broken' )
        
        label3.grid()
        result3.grid()
        result3.current(1)
        
        ##
        label4 = tk.Label(
            self,
            text="Attached Leadership at:")
        tr4 = tk.StringVar()
        result4 = ttk.Combobox(
            self,
            height=2,
            textvariable=tr4
            )
        result4['values'] = ("None",
            "Charismatic Div or Brig",
            "Charismatic Reg or below",
            "Inspiring Div or Brig",
            "Inspiring Reg or below",
            "Fine Unit leader attached to sub unit",
            "Contemptible Div or Brig",
            "Contemptible Reg or below"
            )
        
        label4.grid()
        result4.grid()
        result4.current(1)       

##
        label5 = tk.Label(
            self,
            text="Unit is attacking:")
        tr5 = tk.StringVar()
        result5 = ttk.Combobox(
            self,
            height=1,
            textvariable=tr5
            )
        result5['values'] = ("with no advantage",
            "the Flank",
            "the Rear",
            "with Partial Enfilade",
            "with Full Enfilade"
            )
        
        label5.grid()
        result5.grid()
        result5.current(1)       

###############
# Execute App #
###############
if __name__ == '__main__':
    root = CAC_Window()
    root.mainloop() 
