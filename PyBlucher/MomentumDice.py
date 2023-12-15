import dice

##momentumRemaining = int(xdice.roll('3d6'))
##
##print('Begin Turn')
##print('Activate by corps')
##
##while momentumRemaining > 0:
##    unitsActivated = input('enter number of units activated in this Corps. 0 to end corps activations: ')
##    unitsActivated = int(unitsActivated)
##    if unitsActivated == 0:
##        print('Activate by individual units')
##        while momentumRemaining > 0:
##            unitActivated = input('y to activate one unit, c to activate by CinC and end turn: ')
##            if unitActivated == 'y':
##               momentumRemaining = momentumRemaining - 2
##            if unitActivated == 'c':
##               print('CinC activation')
##               momentumRemaining = 0
##    else:
##        momentumRemaining = momentumRemaining - unitsActivated
##    if momentumRemaining > 0:
##        print('continue')
##    else:
##        print('Turn ended')
##

class MomentumDice():
##  phase 1 is activate by Corp
##  phase 2 is activate individual units
    def __init__(self):
        
        self.momentumRemaining = int(dice.roll('3d6'))
        self.momentumPhase = 1

    def ifValidForCorpActivate(self):
        if self.momentumPhase == 1 and self.momentumRemaining > 0:
            return True
        else:
            return False

    def activateCorp(self, unitsActivated):
        unitActivated = int(unitsActivated)
        self.momentumRemaining = self.momentumRemaining - unitActivated

    def activateUnit(self):
        self.momentumRemaining = self.momentumRemaining - 2

    def turnActive(self):
        if self.momentumRemaining > 0:
            return True
        else:
            return False
			
    def getMomentumRemaining(self):
        return self.momentumRemaining
		
		
    def setCinCActivation(self):
        self.momentumRemaining = 0
        return
		
        
