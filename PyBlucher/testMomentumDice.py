from MomentumDice import *


myMomentum = MomentumDice()

print('Begin Turn')

print('Activate by corps')

while myMomentum.ifValidForCorpActivate():
        if myMomentum.turnActive():  
                print('Activate by corps')
                unitsActivated = input('enter number of units activated in this Corps. 0 to end corps activations: ')
                unitsActivated = int(unitsActivated)
                if unitsActivated == 0:
                        print('Activate by individual units')
                        while myMomentum.turnActive():
                                unitActivated = input('y to activate one unit or c to activate by C-in-C and end turn')
                                if unitActivated == 'y':
                                        print('Unit activation')
                                        myMomentum.activateUnit()
                                elif unitActivated == 'c':
                                        print('CinC activation')
                                        myMomentum.setCinCActivation()
                else:
                        myMomentum.activateCorp(unitsActivated)
                        print('TEST remaining momentum:', myMomentum.getMomentumRemaining())
       
print('Momentum exhausted')
