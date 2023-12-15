import dice

# MomentumDice class is has methods that are applied to a Momntum Dice roll.

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

    def ifTurnActive(self):
        if self.momentumRemaining > 0:
            return True
        else:
            return False
			
    def getMomentumRemaining(self):
        return self.momentumRemaining
		
		
    def CinCActivation(self):
        self.momentumRemaining = 0
        return

    def deactivateCorp(self):
        self.momentumPhase = 2
        return
		
        
