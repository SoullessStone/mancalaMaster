from gamemodel import GameModel

class Game:
    __turn = 0;
    __MAX_TURN = 0;
    __MIN_TURN = 1;
    gameModel = None;

    # Returns, if it is the turn of MAX
    def isMaxTurn(self):
        return self.__turn == self.__MAX_TURN;
    
    # Returns, if it is the turn of MIN
    def isMinTurn(self):
        return self.__turn == self.__MIN_TURN;
    
    # Returns the initial state
    def start(self):
        return GameModel();
    
    # Do a move on current state
    def doMove(self, move):
        raise NotImplementedError("You should have implemented this");
    
    # Returns the last move leading to this state
    def getLastMove(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns all possible moves of this state
    def getPossibleMoves(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns all successor states
    def expand(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns, if the current state is terminal
    def isTerminal(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns the evaluation of a state related to MAX
    def evalValueForMax(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns the evaluation for a terminal state (for MAX)
    def utility(self):
        raise NotImplementedError("You should have implemented this");
    
    def __init__(self):
        self.gameModel = GameModel();
        


print(Game().start());
