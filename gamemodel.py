class GameModel:
    # Indices for fields
    PLAYER1_1 = 0;
    PLAYER1_2 = 1;
    PLAYER1_3 = 2;
    PLAYER1_4 = 3;
    PLAYER1_5 = 4;
    PLAYER1_6 = 5;
    PLAYER1_BASE = 6;
    PLAYER2_1 = 7;
    PLAYER2_2 = 8;
    PLAYER2_3 = 9;
    PLAYER2_4 = 10;
    PLAYER2_5 = 11;
    PLAYER2_6 = 12;
    PLAYER2_BASE = 13;
    
    __gamefield=[4,4,4,4,4,4,
               0,
               4,4,4,4,4,4,
               0];
    
    __turn = 0;
        
    def __init__(self):
        print("new Game created");
    
    def getTurn(self):
        return self.__turn;
    
    def switchTurn(self):
        if self.__turn == 1:
            self.__turn = 0;
        else:
            self.__turn = 1;
    
    def getFieldValue(self,position):
        return self.__gamefield[position];
    
    def changeFieldValue(self,position,newValue):
        self.__gamefield[position] = newValue;

    def getGamefield(self):
        return self.__gamefield;

    def printGamefield(self):
        print("gamefield=" + str(self.__gamefield));
