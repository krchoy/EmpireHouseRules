import unittest
from MomentumDice import *

class testMomentumDice(unittest.TestCase):
    # test for the MomentumDice class

    def test_1_initial_values(self):
        
        myMD = MomentumDice()
        self.assertTrue(int(myMD.getMomentumRemaining()) >= 0)
        self.assertTrue(int(myMD.getMomentumRemaining()) <= 18)







if __name__ == '__main__':
    unittest.main()
