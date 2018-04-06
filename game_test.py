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

    def test_isFieldOnCurrentPlayerSide_Player1_0(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(0);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player1_1(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(1);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player1_2(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(2);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player1_3(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(3);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player1_4(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(4);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player1_5(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(5);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player1_6(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(6);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_7(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(67);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_8(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(8);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_8(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(9);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_10(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(10);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_11(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(11);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_12(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(12);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_13(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(13);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player1_14(self):
        sut = Game();

        result = sut.isFieldOnCurrentPlayerSide(14);        

        print("isFieldOnCurrentPlayerSide: " + str(result))

    def test_isFieldOnCurrentPlayerSide_Player2_0(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(0);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_1(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(1);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_2(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(2);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_3(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(3);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_4(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(4);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_5(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(5);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_6(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(6);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_7(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(7);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player2_8(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(8);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player2_8(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(9);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player2_10(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(10);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player2_11(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(11);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player2_12(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(12);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertTrue(result)

    def test_isFieldOnCurrentPlayerSide_Player2_13(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(13);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
        self.assertFalse(result)

    def test_isFieldOnCurrentPlayerSide_Player2_14(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.isFieldOnCurrentPlayerSide(14);        

        print("isFieldOnCurrentPlayerSide: " + str(result))
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


    def test_doMove_Player1_lastBeanOnEmpty(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 1); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 0);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(6, 2); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 1);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 9999999);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.changeFieldValue(13, 0);
        
        sut.gameModel.printGamefield();
        sut.doMove(0);
        sut.gameModel.printGamefield();
        result = sut.gameModel.getGamefield();

        self.assertEquals([0,0,1,1,1,1,2+9999999+1,1,1,1,1,0,1,0], result)


    def test_doMove_Player2_lastBeanOnEmpty(self):
        sut = Game();
        sut.gameModel.changeFieldValue(0, 1); # Player 1 moves
        sut.gameModel.changeFieldValue(1, 8888);
        sut.gameModel.changeFieldValue(2, 1);
        sut.gameModel.changeFieldValue(3, 1);
        sut.gameModel.changeFieldValue(4, 1);
        sut.gameModel.changeFieldValue(5, 1); 
        sut.gameModel.changeFieldValue(6, 0); 
        sut.gameModel.changeFieldValue(7, 1); # Player 2 moves
        sut.gameModel.changeFieldValue(8, 3);
        sut.gameModel.changeFieldValue(9, 1);
        sut.gameModel.changeFieldValue(10, 1);
        sut.gameModel.changeFieldValue(11, 0);
        sut.gameModel.changeFieldValue(12, 1);
        sut.gameModel.changeFieldValue(13, 88);
        
        sut.gameModel.printGamefield();
        sut.gameModel.switchTurn();
        sut.doMove(8);
        sut.gameModel.printGamefield();
        result = sut.gameModel.getGamefield();

        self.assertEquals([1,0,1,1,1,1,0,1,0,2,2,0,1,88+8888+1], result)

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


    def test_getOpposingField_Player1_1(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER1_1);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_6, result)


    def test_getOpposingField_Player1_2(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER1_2);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_5, result)


    def test_getOpposingField_Player1_3(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER1_3);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_4, result)


    def test_getOpposingField_Player1_4(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER1_4);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_3, result)


    def test_getOpposingField_Player1_5(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER1_5);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_2, result)


    def test_getOpposingField_Player1_6(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER1_6);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_1, result)


    def test_getOpposingField_Player2_1(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER2_1);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_6, result)


    def test_getOpposingField_Player2_2(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER2_2);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_5, result)


    def test_getOpposingField_Player2_3(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER2_3);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_4, result)


    def test_getOpposingField_Player2_4(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER2_4);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_3, result)


    def test_getOpposingField_Player2_5(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER2_5);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_2, result)


    def test_getOpposingField_Player2_6(self):
        sut = Game();

        result = sut.getOpposingField(sut.gameModel.PLAYER2_6);        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_1, result)


    def test_getCurrentPlayerBase_Player1(self):
        sut = Game();

        result = sut.getCurrentPlayerBase();        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER1_BASE, result)


    def test_getCurrentPlayerBase_Player2(self):
        sut = Game();
        sut.gameModel.switchTurn();

        result = sut.getCurrentPlayerBase();        

        print("getOpposingField: " + str(result))
        self.assertEquals(sut.gameModel.PLAYER2_BASE, result)

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
