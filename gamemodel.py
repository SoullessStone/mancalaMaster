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
    
    __gamefield=[0,0,0,0,0,0,
               0,
               0,0,0,0,0,0,
               0];
    
    def getFieldValue(position):
        return __gamefield[position]
        
    
    def __init__(self):
        print("new Game created");


game = GameModel()
print(game.PLAYER2_BASE)
