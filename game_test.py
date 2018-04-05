import unittest
from game import Game

class TestStringMethods(unittest.TestCase):

    def test_getPossibleMoves_1(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 1); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 1);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 1);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.printGamefield();

        result1 = sut.getPossibleMoves();
        sut.gameModel.switchTurn();
        result2 = sut.getPossibleMoves();
        
        print("possible Moves 1: " + str(result1))
        print("possible Moves 2: " + str(result2))
        self.assertEqual([0,1,2,3,4,5], result1)
        self.assertEqual([7,8,9,10,11,12], result2)

    def test_getPossibleMoves_2(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 0); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 1);
        sut.gameModel.changeFieldValue(2, 0);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 0);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 0);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.printGamefield();

        result1 = sut.getPossibleMoves();
        sut.gameModel.switchTurn();
        result2 = sut.getPossibleMoves();
        
        print("possible Moves 1: " + str(result1))
        print("possible Moves 2: " + str(result2))
        self.assertEqual([1,3,4,5], result1)
        self.assertEqual([7,9,10,12], result2)

    def test_isTerminal_no(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 1); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 1);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 1);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.printGamefield();

        result = sut.isTerminal();        

        print("isTerminal: " + str(result))
        self.assertFalse(result)

    def test_isTerminal_true1(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 0); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 0);
        sut.gameModel.changeFieldValue(2, 0);
        sut.gameModel.changeFieldValue(3, 0);
        sut.gameModel.changeFieldValue(4, 0);
        sut.gameModel.changeFieldValue(5, 0); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 1);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.printGamefield();

        result = sut.isTerminal();        

        print("isTerminal: " + str(result))
        self.assertTrue(result)

    def test_isTerminal_true2(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 1); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 2);
        sut.gameModel.changeFieldValue(2, 2);
        sut.gameModel.changeFieldValue(3, 2);
        sut.gameModel.changeFieldValue(4, 2);
        sut.gameModel.changeFieldValue(5, 2); 
        sut.gameModel.changeFieldValue(7, 0); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 0);
        sut.gameModel.changeFieldValue(9, 0);
        sut.gameModel.changeFieldValue(10, 0);
        sut.gameModel.changeFieldValue(11, 0);
        sut.gameModel.changeFieldValue(12, 0);
        sut.gameModel.printGamefield();

        result = sut.isTerminal();        

        print("isTerminal: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_0(self):
        sut = Game();

        result = sut.isLegalMove(0);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_1(self):
        sut = Game();

        result = sut.isLegalMove(1);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_2(self):
        sut = Game();

        result = sut.isLegalMove(2);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_3(self):
        sut = Game();

        result = sut.isLegalMove(3);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_4(self):
        sut = Game();

        result = sut.isLegalMove(4);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_5(self):
        sut = Game();

        result = sut.isLegalMove(5);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player1_6(self):
        sut = Game();

        result = sut.isLegalMove(6);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_7(self):
        sut = Game();

        result = sut.isLegalMove(67);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_8(self):
        sut = Game();

        result = sut.isLegalMove(8);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_8(self):
        sut = Game();

        result = sut.isLegalMove(9);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_10(self):
        sut = Game();

        result = sut.isLegalMove(10);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_11(self):
        sut = Game();

        result = sut.isLegalMove(11);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_12(self):
        sut = Game();

        result = sut.isLegalMove(12);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_13(self):
        sut = Game();

        result = sut.isLegalMove(13);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player1_14(self):
        sut = Game();

        result = sut.isLegalMove(14);        

        print("isLegalMove: " + str(result))

    def test_isLegalMove_Player2_0(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(0);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_1(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(1);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_2(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(2);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_3(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(3);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_4(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(4);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_5(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(5);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_6(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(6);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_7(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(7);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_8(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(8);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_8(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(9);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_10(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(10);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_11(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(11);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_12(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(12);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_13(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(13);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_14(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isLegalMove(14);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_doMove_simple(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 7); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 1);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(6, 0); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 1);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.changeFieldValue(13, 0);
        
        sut.gameModel.printGamefield();
        sut.doMove(0);
        sut.gameModel.printGamefield();
        result = sut.gameModel.getGamefield();

        self.assertEquals([0, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 0], result)

    def test_doMove_Player1_dont_change_base_2(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 14); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 1);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(6, 0); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 1);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.changeFieldValue(13, 0);
        
        sut.gameModel.printGamefield();
        sut.doMove(0);
        sut.gameModel.printGamefield();
        result = sut.gameModel.getGamefield();

        self.assertEquals([1, 3, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0], result)

    def test_doMove_Player2_dont_change_base_1(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 1); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 1);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(6, 0); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 1);
        sut.gameModel.changeFieldValue(12, 8);
        sut.gameModel.changeFieldValue(13, 0);
        
        sut.gameModel.switchTurn();
        sut.gameModel.printGamefield();
        sut.doMove(12);
        sut.gameModel.printGamefield();
        result = sut.gameModel.getGamefield();

        self.assertEquals([2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 1, 1, 0, 1], result)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
